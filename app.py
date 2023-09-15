from flask import Flask, render_template, request
import random

app = Flask(__name__)

hour = ["Deep dive whatshouldido app! :]"]
thirty_min = ["Code wars (hard)", "Code Wars (Easy)"]
fifteen_min = ["Code wars (medium)"]
five_min = ["Code wars (easy)"]

time_left = 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    study_time = request.form.get("time-mins")
    time_left = study_time
    if time_left > 120:
        #print("You could do " + random.choice(hour) + ", " + random.choice(thirty_min) + ", " + "and some small stuff like " + random.choice(fifteen_min) + ".")
       # print paragraph("wow that's a lot of time to study. Here are some of the things you could do:")
    elif time_left < 120 and study_time > 60:
        time_left = study_time - 60
        print("hard or long stuff")
    return render_template("results.html", study_time = study_time)