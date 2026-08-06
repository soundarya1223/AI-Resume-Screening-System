def calculate_match(resume_skills, job_skills):

    matched_skills = []

    for skill in resume_skills:
        if skill in job_skills:
            matched_skills.append(skill)


    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_skills)) * 100


    return {
        "score": round(score, 2),
        "matched": matched_skills,
        "missing": list(set(job_skills) - set(matched_skills))
    }