from models.ai_matcher import calculate_similarity


resume = """
Java developer with SQL database experience.
Built backend applications using Flask.
"""


job = """
Looking for a backend developer skilled in Java,
SQL and web application development.
"""


score = calculate_similarity(
    resume,
    job
)


print("AI Match Score:", score, "%")