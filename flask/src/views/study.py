from flask import Blueprint, render_template

# Blueprintのオブジェクトを生成する
study = Blueprint('study', __name__, url_prefix="/study")


@study.route('/index')
def func():
    return render_template("sample.html", msg="from Flask")


@study.route('/study1')
def study1():
    return render_template("study1.html")
