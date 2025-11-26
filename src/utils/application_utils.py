import os, json

def save_application_bundle(resume_name, job_id, tailored_output, cover_letter):
    os.makedirs("out/applications", exist_ok=True)
    bundle = {
        "tailored_resume": tailored_output,
        "cover_letter": cover_letter
    }
    file_path = f"out/applications/{resume_name}_{job_id}.json"
    with open(file_path, "w") as f:
        json.dump(bundle, f, indent=2)
    return file_path
