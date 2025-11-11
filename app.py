from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

DATA_PATH = os.environ.get("DATA_PATH", "./data/capstone.json")

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
@app.route("/main")
def main_page():
    data = load_data()
    return render_template("main.html", data=data)

@app.route("/subject")
def subject_page():
    data = load_data()
    return render_template("subject.html", data=data["subject"])

@app.route("/rationale")
def rationale_page():
    data = load_data()
    return render_template("rationale.html", data=data["rationale"])

@app.route("/features")
def features_page():
    data = load_data()
    return render_template("features.html", data=data["features"])

@app.route("/environment")
def environment_page():
    data = load_data()
    return render_template("environment.html", data=data["environment"])

@app.route("/team")
def team_page():
    data = load_data()
    return render_template("team.html", data=data["team"])

@app.route("/api/data")
def api_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
