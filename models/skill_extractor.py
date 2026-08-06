import re


def extract_skills(text):

    skills = {
        "python(project experience)": "Python",
        "core java": "Core Java",
        "sql": "SQL",
        "c": "C",
        "c++": "C++",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
        "flask": "Flask",
        "django": "Django",
        "mongodb": "MongoDB",
        "mysql": "MySQL",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript",
        "react": "React",
        "git": "Git",
        "docker": "Docker",
        "aws": "AWS"
    }


    found_skills = []

    text = text.lower()


    # Remove special characters but keep letters
    text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)


    for skill, display_name in skills.items():

        if skill.lower() in text:

            found_skills.append(display_name)


    return found_skills