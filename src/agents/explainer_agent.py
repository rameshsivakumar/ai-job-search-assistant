import json
from src.utils.llm import call_gemini

class ExplainerAgent:

    def __init__(self):
        pass

    def explain_match(self, resume_json, job_json, match_details):
        """
        match_details = {
            "skill_overlap": "4/7",
            "skill_overlap_list": ["python", "sql"],
            "seniority_penalty": 0,
            "location_score": 1,
            "remote_score": 1
        }
        """
        prompt = f"""
MATCH_EXPLAIN
Explain in clear language why this candidate matches this job.

Requirements:
- 3 sections: "Match Summary", "Skill Analysis", "Recommendations"
- Explain in simple short bullet points.
- Only mention skills from the job description.
- Highlight gaps clearly.
- Keep ATS-friendly, plain text only.

Resume JSON:
{json.dumps(resume_json, indent=2)}

Job JSON:
{json.dumps(job_json, indent=2)}

Match Details JSON:
{json.dumps(match_details, indent=2)}
"""

        return call_gemini(prompt, temperature=0.3)
