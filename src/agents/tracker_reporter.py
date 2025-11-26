import csv
from src.agents.tracker_agent import ApplicationTrackerAgent

class TrackerReporter:

    def __init__(self, tracker_file="data/applications.jsonl"):
        self.tracker = ApplicationTrackerAgent(tracker_file)

    def export_csv(self, out_path="out/application_report.csv"):
        import os
        os.makedirs("out", exist_ok=True)

        records = self.tracker.read_all()

        with open(out_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "timestamp", "resume_name", "job_id", "status"])
            for r in records:
                writer.writerow([
                    r["id"],
                    r["timestamp"],
                    r["resume_name"],
                    r["job_id"],
                    r["status"]
                ])
        return out_path
