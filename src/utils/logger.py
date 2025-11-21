import json, os, time

SEARCH_LOG = "logs/search_log.jsonl"
os.makedirs("logs", exist_ok=True)

def log_search(query, filters, results):
    entry = {
        "timestamp": time.time(),
        "query": query,
        "filters": filters,
        "results": [job.id for job in results]
    }
    with open(SEARCH_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
