from flask import Flask, render_template, request

app = Flask(__name__)

hour = []
thirty_min = ["Code wars (hard)", "Code Wars (Easy)"]
fiften_min = []
five_min = []

study_time = 0
time_left = 0

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        study_time, time_left = request.form.get("content")
        if time_left > 120:
            print("wow that's a lot of time to study. Here are some of the things you could do:")
        elif time_left < 120 and study_time > 60:
            time_left = study_time - 60
            print("hard or long stuff")

    return render_template("home.html")