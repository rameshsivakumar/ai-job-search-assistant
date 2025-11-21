from typing import List, Dict
from src.models.job import Job

class SearchAgent:

    def __init__(self, jobs: List[Job]):
        self.jobs = jobs

    def search(self, query: str = "", filters: Dict = None, top_k: int = 20) -> List[Job]:
        filters = filters or {}
        q = query.lower().strip()

        scored = []

        for job in self.jobs:
            score = 0

            # Keyword matching on title & description
            if q:
                if q in job.title.lower() or q in job.description.lower():
                    score += 3
                elif q in job.company.lower():
                    score += 2

            # Location match
            if "location" in filters:
                if filters["location"].lower() in job.location.lower():
                    score += 1

            # Remote filter
            if "remote" in filters:
                if filters["remote"] == job.remote:
                    score += 1

            # Skills filter
            if "skills" in filters:
                rs = {s.lower() for s in filters["skills"]}
                js = {s.lower() for s in job.skills}
                score += len(rs & js)  # add 1 per skill match

            scored.append((score, job))

        # Sort by score desc
        scored = sorted(scored, key=lambda x: x[0], reverse=True)
        return [job for score, job in scored[:top_k]]
