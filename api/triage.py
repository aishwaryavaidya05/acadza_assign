"""Vercel serverless function: POST /api/triage  {questionId, comment} -> live verdict (dry run, never applied)."""
import json, os, sys, time, pathlib
from collections import Counter
from http.server import BaseHTTPRequestHandler
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import engine

_err = None
try:
    _Q = {q["_id"]: q for q in json.load(open(engine.DATA / "questions.json"))}
    _TAX = json.load(open(engine.DATA / "taxonomy.json"))
    _QC = Counter(q.get("qid") for q in _Q.values())
    _SP = engine.DATA / "solves.json"
    _STORE = json.load(open(_SP)) if _SP.exists() else {}
except Exception as e:  # missing data files etc.
    _err = str(e)
_HITS = {}   # best-effort per-instance limiter; your Gemini quota is the real cap

def _limited(ip):
    now = time.time(); h = [t for t in _HITS.get(ip, []) if now - t < 3600]
    if len(h) >= int(os.getenv("HOURLY_LIMIT", "20")): _HITS[ip] = h; return True
    h.append(now); _HITS[ip] = h; return False

class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)

    def do_POST(self):
        if _err: return self._send(500, {"error": "server_data_missing"})
        try:
            n = int(self.headers.get("content-length", 0))
            if n > 4000: return self._send(413, {"error": "too_large"})
            d = json.loads(self.rfile.read(n) or b"{}")
        except Exception: return self._send(400, {"error": "bad_request"})
        ip = (self.headers.get("x-forwarded-for") or "?").split(",")[0].strip()
        if _limited(ip): return self._send(429, {"error": "rate_limited"})
        q = _Q.get(d.get("questionId"))
        comment = "".join(ch for ch in str(d.get("comment", "")) if ch.isprintable())[:300].strip()
        if not q or not comment: return self._send(400, {"error": "bad_input"})
        try:
            res, extra = engine.triage_one({"reportId": "LIVE", "comment": comment}, q, _TAX, _QC, _STORE)
        except RuntimeError as e:
            return self._send(503 if str(e) in ("no_key",) or str(e).startswith("http_429") else 502, {"error": str(e)})
        except Exception:
            return self._send(502, {"error": "upstream_failed"})
        return self._send(200, {"live": True, "model": engine.MODEL, "result": res, "extra": extra})
