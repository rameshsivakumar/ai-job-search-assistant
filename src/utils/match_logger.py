import json, time, os
os.makedirs("logs", exist_ok=True)

MATCH_LOG = "logs/match_log.jsonl"

def log_match(resume_name, results):
    entry = {
        "timestamp": time.time(),
        "resume": resume_name,
        "results": [
            {
                "job_id": r["job"].id,
                "score": r["score"],
                "explanation": r["explanation"]
            }
            for r in results
        ]
    }
    with open(MATCH_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
