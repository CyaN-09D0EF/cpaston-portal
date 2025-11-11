from flask import Blueprint, render_template
from data_access import read_json

web_bp = Blueprint("web", __name__)

@web_bp.get("/main")
def main_page():
    data = read_json()
    return render_template("main.html", data=data)

@web_bp.get("/subject")
def subject_page():
    data = read_json()
    return render_template("subject.html", data=data)

@web_bp.get("/rationale")
def rationale_page():
    data = read_json()
    return render_template("rationale.html", data=data)

@web_bp.get("/features")
def features_page():
    data = read_json()
    return render_template("features.html", data=data)

@web_bp.get("/environment")
def environment_page():
    data = read_json()
    return render_template("environment.html", data=data)

@web_bp.get("/team")
def team_page():
    data = read_json()
    return render_template("team.html", data=data)

# 기본 루트는 /main으로 리다이렉트
@web_bp.get("/")
def root():
    from flask import redirect, url_for
    return redirect(url_for("web.main_page"))
