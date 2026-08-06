def generate_recommendation(missing_skills):

    if not missing_skills:
        return "Excellent! Your resume matches all required skills."

    skills = ", ".join(missing_skills)

    return f"Consider improving your knowledge in: {skills}"