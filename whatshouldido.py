from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    entries = []

    @app.route("/", methods=["GET", "POST"])
    def home():
        return render_template("home.html")
    return app