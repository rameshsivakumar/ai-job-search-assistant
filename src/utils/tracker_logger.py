import json, time, os
os.makedirs("logs", exist_ok=True)

TRACKER_LOG = "logs/tracker_log.jsonl"

def log_tracker_event(event_type, record):
    entry = {
        "timestamp": time.time(),
        "event_type": event_type,
        "record": record
    }
    with open(TRACKER_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
