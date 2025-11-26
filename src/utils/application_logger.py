import json, time, os
os.makedirs("logs", exist_ok=True)

APP_LOG = "logs/application_log.jsonl"

def log_application(resume_name, job_id, cover_letter):
    entry = {
        "timestamp": time.time(),
        "resume": resume_name,
        "job_id": job_id,
        "cover_letter_excerpt": cover_letter[:250]
    }
    with open(APP_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
