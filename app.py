from flask import Flask, render_template, request
import os

from models.parser import extract_text
from models.cleaner import clean_text
from models.skill_extractor import extract_skills
from models.matcher import calculate_match


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["resume"]

        if file:

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    file.filename
                )
            )

            return render_template("analyze.html")


    return render_template("upload.html")



@app.route("/analyze", methods=["POST"])
def analyze():

    job_description = request.form["job_description"]


    resume_file = os.listdir("uploads")[0]


    resume_path = os.path.join(
        "uploads",
        resume_file
    )


    resume_text = extract_text(resume_path)

    cleaned_text = clean_text(resume_text)


    resume_skills = extract_skills(cleaned_text)


    job_skills = extract_skills(job_description)


    result = calculate_match(
        resume_skills,
        job_skills
    )


    return render_template(
        "result.html",
        score=result["score"],
        matched=result["matched"],
        missing=result["missing"]
    )



if __name__ == "__main__":
    app.run(debug=True)