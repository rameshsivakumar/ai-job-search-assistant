import json
from src.utils.llm import call_gemini

class ApplicationAgent:

    def __init__(self):
        pass

    def generate_cover_letter(self, resume_json, job_json, tailored_bullets):
        prompt = f"""
COVER_LETTER
Write a personalized cover letter.

Requirements:
- Output plain text (string), not JSON.
- 3–4 short paragraphs.
- Reflect the candidate's tailored resume bullets.
- Use a confident, professional tone.
- Mention the company name and job title.
- Insert keywords from job description.
- ATS friendly (no fancy symbols or formatting).

Candidate Resume (JSON):
{json.dumps(resume_json, indent=2)}

Job Description (JSON):
{json.dumps(job_json, indent=2)}

Tailored Bullets (JSON):
{json.dumps(tailored_bullets, indent=2)}
"""

        return call_gemini(prompt, temperature=0.4)
