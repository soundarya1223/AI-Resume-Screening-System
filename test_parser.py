from models.matcher import calculate_match


resume_skills = [
    "python",
    "sql",
    "flask"
]


job_skills = [
    "python",
    "sql",
    "machine learning",
    "flask"
]


result = calculate_match(
    resume_skills,
    job_skills
)


print(result)