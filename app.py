from flask import Flask, render_template, request
import random

app = Flask(__name__)

hour = ["Deep dive whatshouldido app!", "Data Stuctures problems."]
thirty_min = ["Code wars (hard)", "flask bootcamp video with practice afterwards"]
fifteen_min = ["Code wars (medium)", "a flask tutorial video", "a django tutorial video"]
five_min = ["Code wars (easy)", "short tutorial video", "look up something you don't know"]

time_left = 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    study_time = int(request.form.get("time-mins"))
    if study_time > 120:
        time_left = study_time - 120
        result = ("You could do " + random.choice(hour) + ", " + random.choice(thirty_min) + ", " + "and some small stuff like " + random.choice(fifteen_min) + ". " + 
                  "You would still have " + str(time_left) + " minutes left!")
    elif study_time < 120 and study_time > 60:
        study_time -= 60
        print("hard or long stuff")
    return render_template("results.html", study_time = study_time, result = result)