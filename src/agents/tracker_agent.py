import json, os, time, uuid

class ApplicationTrackerAgent:

    def __init__(self, file_path="data/applications.jsonl"):
        self.file_path = file_path
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()

    def add_application(self, resume_name, job_id, tailored_resume, cover_letter):
        record = {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "resume_name": resume_name,
            "job_id": job_id,
            "status": "applied",
            "tailored_resume": tailored_resume,
            "cover_letter": cover_letter
        }
        with open(self.file_path, "a") as f:
            f.write(json.dumps(record) + "\n")
        return record

    def read_all(self):
        records = []
        with open(self.file_path, "r") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        return records

    def update_status(self, application_id, new_status):
        records = self.read_all()
        updated = False
        for r in records:
            if r["id"] == application_id:
                r["status"] = new_status
                updated = True

        if updated:
            with open(self.file_path, "w") as f:
                for r in records:
                    f.write(json.dumps(r) + "\n")

        return updated

    def get_by_resume(self, resume_name):
        return [r for r in self.read_all() if r["resume_name"] == resume_name]

    def get_by_job(self, job_id):
        return [r for r in self.read_all() if r["job_id"] == job_id]
