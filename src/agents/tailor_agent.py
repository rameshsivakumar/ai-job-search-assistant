import json
from src.utils.llm import call_gemini

class TailorAgent:

    def __init__(self):
        pass

    def generate_bullets(self, resume_json, job_json):
        prompt = f"""
TAILOR_BULLETS
Rewrite the candidate's resume bullets to match the job description.

Rules:
- Output ONLY valid JSON.
- Use achievement-style bullet points.
- Max 6 bullets.
- Include keywords from the job description.
- Keep it ATS-friendly, no fancy formatting.
- Use strong action verbs.
- Reflect relevant skills ONLY.

Return JSON:
{{
  "summary": "<2-3 sentence summary>",
  "bullets": ["...", "...", ...],
  "inserted_keywords": ["...", "..."]
}}

Candidate Resume JSON:
{json.dumps(resume_json, indent=2)}

Job Description JSON:
{json.dumps(job_json, indent=2)}
"""

        raw = call_gemini(prompt, temperature=0.3)
        try:
            return json.loads(raw)
        except:
            # fallback: prompt again with stricter instructions
            raw2 = call_gemini(prompt + "\nEnsure you output strictly valid JSON.", temperature=0)
            return json.loads(raw2)
