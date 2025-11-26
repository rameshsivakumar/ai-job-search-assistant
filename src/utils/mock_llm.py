import json

def mock_call_gemini(prompt: str, temperature: float = 0.0, max_tokens: int = 512) -> str:
    """
    Deterministic mock of Gemini used during offline development.
    Replace with real Gemini API calls later.
    """

    # Resume extraction
    if "EXTRACT_RESUME_JSON" in prompt:
        return json.dumps({
            "name": "Mock Candidate",
            "title": "Software Engineer",
            "emails": ["mock@example.com"],
            "phones": ["+91 90000 11111"],
            "skills": ["Python", "Java", "SQL"],
            "years_experience": 3,
            "experience": [
                {
                    "title": "Software Engineer",
                    "company": "MockCorp",
                    "start": "2021-01",
                    "end": "2024-01",
                    "bullets": ["Worked on mock features."]
                }
            ],
            "education": ["B.Tech Computer Science"]
        })

    # Tailor bullets
    if "TAILOR_BULLETS" in prompt:
        return json.dumps({
            "summary": "Experienced developer skilled in delivering backend services.",
            "bullets": [
                "Developed mock microservices using Python and Java.",
                "Improved API performance through caching strategies.",
                "Integrated SQL databases for faster data access."
            ],
            "inserted_keywords": ["Python", "SQL", "microservices"]
        })

    # Cover letters
    if "COVER_LETTER" in prompt:
        return "Dear Hiring Manager,\n\nI am excited to apply for the role...\n"

    # Match explanations
    if "MATCH_EXPLAIN" in prompt:
        return json.dumps({
            "match_score": 0.74,
            "reasons": ["Matches 4/5 required skills"],
            "gaps": ["Needs more experience with microservices"]
        })

    # Default fallback
    return json.dumps({"response": "[MOCK RESPONSE]"})

