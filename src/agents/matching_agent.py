from typing import List, Dict
from src.models.job import Job
import math

class MatchingAgent:

    def __init__(self, weight_skill=0.6, weight_seniority=0.3, weight_location=0.1, weight_remote=0.1):
        self.w_skill = weight_skill
        self.w_seniority = weight_seniority
        self.w_location = weight_location
        self.w_remote = weight_remote

    def _skill_score(self, resume_skills, job_skills):
        if not job_skills:
            return 0
        r = {s.lower() for s in resume_skills}
        j = {s.lower() for s in job_skills}
        overlap = r & j
        return len(overlap) / len(j), list(overlap)

    def _seniority_penalty(self, resume_years, job_seniority):
        if job_seniority == "senior" and resume_years < 5:
            return 1
        if job_seniority == "mid" and resume_years < 2:
            return 0.5
        return 0

    def _location_score(self, resume_location, job_location):
        if not resume_location:
            return 0
        return 1 if resume_location.lower() in job_location.lower() else 0

    def _remote_score(self, user_pref_remote, job_remote):
        if user_pref_remote is None:
            return 0
        return 1 if user_pref_remote == job_remote else 0

    def match(self, resume_json: Dict, jobs: List[Job], top_k=10, user_pref=None):
        user_pref = user_pref or {}
        resume_skills = resume_json.get("skills", [])
        resume_years = resume_json.get("years_experience", 0)
        resume_location = resume_json.get("location", "")

        pref_remote = user_pref.get("remote")

        scored = []

        for job in jobs:
            # 1. Skill score
            skill_score, skill_overlap = self._skill_score(resume_skills, job.skills)

            # 2. Seniority penalty
            seniority_pen = self._seniority_penalty(resume_years, job.seniority)

            # 3. Location
            location_score = self._location_score(resume_location, job.location)

            # 4. Remote preference
            remote_score = self._remote_score(pref_remote, job.remote)

            # Final score
            final = (
                skill_score * self.w_skill
                - seniority_pen * self.w_seniority
                + location_score * self.w_location
                + remote_score * self.w_remote
            )

            scored.append({
                "job": job,
                "score": round(final, 4),
                "explanation": {
                    "skill_overlap": f"{len(skill_overlap)}/{len(job.skills)}",
                    "skill_overlap_list": skill_overlap,
                    "seniority_penalty": seniority_pen,
                    "location_score": location_score,
                    "remote_score": remote_score,
                }
            })

        scored = sorted(scored, key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
