# PROMPTS.md

## Prompts Used During Development

### 1. Project Planning
"Tell me the plan: what to do, how to do it, and how to implement the bonus. Suggest a few approaches for each step. Provide a simple flowchart and explain edge cases, possible errors, and mistakes to keep in mind."

### 2. Frontend and Workflow
"I'm thinking of a two-button approach: the first button shows what the question will look like with the proposed change highlighted, and the second button confirms and applies the fix. Suggest approaches for generating fixes based on the README."

### 3. Fix Recommendation Strategy
"How can I make fix suggestions more reliable and deterministic? Can I use grounding RAG with a narrow domain?"

### 4. Bonus Implementation
"For the bonus question, help me find defects nobody reported. I'm assuming these are questions in `questions.json` that are not present in `reports.json`. How would I submit them and calculate accuracy?"

### 5. LLM Provider Selection
"Should I use an API key for the LLM or host a model locally using Ollama? The project has to run on the reviewer's side as well, so I'm considering deploying it and sharing the deployed link."

"Suggest an LLM with enough free-tier credits to run the benchmark multiple times. Each test contains around 44 examples, with each example requiring 1–2 calls. I don't want to use a credit card."

### 6. LLM Pipeline Implementation
"Give me the frontend (HTML + MathML), LLM pipeline (Python), and the integrated frontend and LLM implementation. Write the LLM script according to the Gemini API."

"I want to use constrained decoding, no thinking, schema-grounded output, and few-shot prompting."

### 7. Model and Performance Improvements
"Can we try another Gemini model? I need this to work quickly, with high schema accuracy and good overall accuracy. Also, why is it getting stuck?"

"Perform all the code changes for correct UTF-8 configuration and switching to the Groq model."

### 8. Benchmarking
"I would like to calculate and save accuracy for each run. I also don't have a `compare.py`. Should I run the full `engine.py`?"

### 9. Deployment
"I'll use the Groq API key and deploy the application on Vercel later. The API key should be configured securely through environment variables."

### 10. Documentation
"Use any AI tools you like. In `PROMPTS.md`, share your prompts verbatim and the key design decisions you made: what you tried, what you dropped, and why. How you think and direct AI matters more to us than whether you use it."