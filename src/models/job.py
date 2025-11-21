from pydantic import BaseModel
from typing import List

class Job(BaseModel):
    id: str
    title: str
    company: str
    location: str
    remote: bool
    skills: List[str]
    seniority: str
    salary: str
    description: str
