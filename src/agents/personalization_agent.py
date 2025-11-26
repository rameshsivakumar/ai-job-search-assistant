from typing import Dict, List

class PersonalizationAgent:

    def __init__(self, w_location=0.15, w_company=0.20, w_role=0.20, w_salary=0.25, w_remote=0.20):
        self.w_location = w_location
        self.w_company = w_company
        self.w_role = w_role
        self.w_salary = w_salary
        self.w_remote = w_remote

    def apply(self, ranked_results: List[Dict], preferences: Dict):
        """Re-ranks results based on user preferences."""

        pref_locs = [l.lower() for l in preferences.get("preferred_locations", [])]
        pref_comps = [c.lower() for c in preferences.get("preferred_companies", [])]
        pref_roles = [r.lower() for r in preferences.get("preferred_roles", [])]
        pref_min_salary = preferences.get("min_salary")
        pref_remote = preferences.get("remote")

        personalized = []

        for item in ranked_results:
            job = item["job"]
            base_score = item["score"]
            bonus = 0
            debug = {}

            # 1. Location preference
            if pref_locs:
                if any(loc in job.location.lower() for loc in pref_locs):
                    bonus += self.w_location
                    debug["location_bonus"] = self.w_location

            # 2. Company preference
            if pref_comps:
                if job.company.lower() in pref_comps:
                    bonus += self.w_company
                    debug["company_bonus"] = self.w_company

            # 3. Role preference (keyword match)
            if pref_roles:
                if any(role in job.title.lower() for role in pref_roles):
                    bonus += self.w_role
                    debug["role_bonus"] = self.w_role

            # 4. Salary preference (extract minimum number from salary string)
            if pref_min_salary:
                try:
                    # assume salary string like "12-18 LPA"
                    min_salary = int(job.salary.split("-")[0])
                    if min_salary >= pref_min_salary:
                        bonus += self.w_salary
                        debug["salary_bonus"] = self.w_salary
                except:
                    pass

            # 5. Remote preference
            if pref_remote is not None:
                if job.remote == pref_remote:
                    bonus += self.w_remote
                    debug["remote_bonus"] = self.w_remote

            personalized.append({
                "job": job,
                "original_score": base_score,
                "personalized_score": round(base_score + bonus, 4),
                "bonus": round(bonus, 4),
                "explanation": {
                    **item["explanation"],
                    "personalization_debug": debug
                }
            })

        # Sort by personalized score descending
        personalized = sorted(personalized, key=lambda x: x["personalized_score"], reverse=True)

        return personalized
