import re, json
from typing import Dict
from pydantic import BaseModel
from datetime import datetime
from src.utils.llm import call_gemini  # or mock_call_gemini

class Resume(BaseModel):
    name: str = None
    title: str = None
    emails: list = []
    phones: list = []
    skills: list = []
    years_experience: int = 0
    experience: list = []
    education: list = []

def extract_years_experience(text):
    # simple heuristic: count years from experience lines
    matches = re.findall(r"(\d{4})", text)
    years = len(set(matches))
    return max(1, years)

def rule_based_parse(text):
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    phones = re.findall(r"\+?\d[\d \-]{7,}\d", text)

    skill_patterns = r"Skills?:?(.*)"
    m = re.search(skill_patterns, text, re.IGNORECASE)
    skills = []
    if m:
        items = re.split(r",|;|\||\n", m.group(1))
        skills = [i.strip() for i in items if len(i.strip()) > 1]

    return {
        "emails": emails,
        "phones": phones,
        "skills": skills
    }

def resume_to_json(resume_text: str) -> Dict:
    # Step 1: try rule-based extraction
    rb = rule_based_parse(resume_text)

    # Step 2: If skills < 3 or missing emails -> call LLM fallback
    if len(rb["skills"]) < 3 or len(rb["emails"]) == 0:
        prompt = f"""
EXTRACT_RESUME_JSON
Extract structured JSON from this resume. Use keys:
name, title, emails, phones, skills, years_experience,
experience (list of {{title, company, start, end, bullets}}),
education (list).
Resume:
{resume_text}
"""
        llm_output = call_gemini(prompt, temperature=0)
        try:
            return json.loads(llm_output)
        except:
            pass  # if LLM fails, fallback to rule-based only

    # Step 3: Build rule-based JSON
    years = extract_years_experience(resume_text)
    return {
        "name": resume_text.split("\n")[0].strip(),
        "title": None,
        "emails": rb["emails"],
        "phones": rb["phones"],
        "skills": rb["skills"],
        "years_experience": years,
        "experience": [],
        "education": []
    }
