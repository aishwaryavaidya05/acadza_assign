# PRODUCT.md

## 1. Who Loses the Most When a Question Is Broken?
Students lose the most because defective questions or incorrect answer keys can affect their performance and understanding. The system identifies reported defects and explores potentially unreported defects using `questions.json` and `reports.json`.
Proposed fixes are displayed with highlighted changes for review before application.

## 2. What Would I Never Let AI Auto-Apply?
I would never allow AI to automatically apply corrections to questions or answer keys.
JEE and NEET questions can involve complex mathematical and scientific concepts that LLMs may misinterpret. Such corrections should be reviewed by subject-matter faculty.
The system therefore requires human confirmation before applying any proposed fix.

## 3. One Metric to Watch in Week 1
**Schema Accuracy**
Track the percentage of LLM responses that conform to the required output schema.
This is particularly important because the pipeline relies on structured responses for validation, defect classification, and frontend integration.

## 4. One Idea Beyond This Brief
**Live Triage**
Allow reviewers to submit a new question or defect report directly through the console and run it through the LLM pipeline. The system would generate a structured verdict and proposed correction, with changes highlighted for review.
Combined with schema accuracy tracking across benchmark runs, this would make the system easier to test, monitor, and improve while keeping final correction decisions with human reviewers.