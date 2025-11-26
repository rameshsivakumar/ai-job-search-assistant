import json, time, os
os.makedirs("logs", exist_ok=True)

EXPLAIN_LOG = "logs/explainer_log.jsonl"

def log_explanation(resume_name, job_id, explanation):
    entry = {
        "timestamp": time.time(),
        "resume": resume_name,
        "job_id": job_id,
        "explanation": explanation
    }
    with open(EXPLAIN_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
