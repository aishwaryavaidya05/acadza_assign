# Report → Fix

Student error reports → Gemini triage (blind solves + verdict + guards) → faculty console.

## Layout
- `engine.py` – the pipeline (Gemini REST, cached). Prompts are at the top of the file.
- `api/triage.py` – Vercel function behind the console's "Try a new report" box (dry run only).
- `public/index.html` – faculty console (static, native MathML). Reads `public/data/*.json`.
- `data/` – put `questions.json`, `reports.json`, `taxonomy.json` here.
- `results.json`, `unreported.json` – engine output (scored file + bonus findings).
- `reference/` – hand-solved benchmark used only for dev comparison, NOT the product output.

## Run locally
```
pip install -r requirements.txt
export GEMINI_API_KEY=...            # free key from aistudio.google.com
python engine.py --limit 5           # smoke test
python engine.py --llm-audit         # full run (+ blind-solve audit for the bonus)
python validate.py                   # schema/scope/find-uniqueness checks
python compare.py                    # accuracy vs hand-solved reference
cd public && python -m http.server 8000   # open http://localhost:8000
```
Responses are cached in `.cache/` (commit it) so reruns are free and reproducible.
Console data is precomputed; the live box needs the deployed function.

## Deploy on Vercel
1. Push the repo (include `public/data/` and `data/solves.json`, **not** your key).
2. Import in Vercel, framework "Other". Add env var `GEMINI_API_KEY` (and optionally `MODEL`, `HOURLY_LIMIT`).
3. If the live function fails or the quota is hit, the console says so and shows the precomputed result.
