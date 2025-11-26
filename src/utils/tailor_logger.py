import json, time, os
os.makedirs("logs", exist_ok=True)

TAILOR_LOG = "logs/tailor_log.jsonl"

def log_tailor(resume_name, job_id, prompt, result):
    entry = {
        "timestamp": time.time(),
        "resume": resume_name,
        "job_id": job_id,
        "prompt_preview": prompt[:300],
        "output": result
    }
    with open(TAILOR_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
