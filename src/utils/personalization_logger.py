import json, time, os
os.makedirs("logs", exist_ok=True)

PERSONAL_LOG = "logs/personalization_log.jsonl"

def log_personalization(resume_name, preferences, results):
    entry = {
        "timestamp": time.time(),
        "resume": resume_name,
        "preferences": preferences,
        "results": [
            {
                "job_id": r["job"].id,
                "personalized_score": r["personalized_score"],
                "bonus": r["bonus"],
                "details": r["explanation"]["personalization_debug"]
            }
            for r in results
        ]
    }
    with open(PERSONAL_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
