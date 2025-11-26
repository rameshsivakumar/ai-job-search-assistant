import os, json

def save_tailored_resume(resume_name, job_id, output):
    os.makedirs("out/resumes", exist_ok=True)
    file_path = f"out/resumes/{resume_name}_{job_id}.json"
    with open(file_path, "w") as f:
        json.dump(output, f, indent=2)
    return file_path
