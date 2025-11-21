import json
from typing import List
from src.models.job import Job

def load_jobs(path="data/jobs.json") -> List[Job]:
    with open(path, "r") as f:
        data = json.load(f)
    return [Job(**job) for job in data]