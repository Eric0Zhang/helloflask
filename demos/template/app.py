# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import os
from flask import Flask, render_template, flash, redirect, url_for, Markup

app = Flask(__name__)
# 获取密码环境变量, 默认secret string 如果不设置密码 flash在调用session时报错: The session is unavailable because no secret key was set.
app.secret_key = os.getenv("SECRET_KEY", "secret string")
# jinja的环境变量, 这两个用来去除block的空白行
app.jinja_env.trim_blocks = True  # If this is set to True the first newline after a block is removed (block, not variable tag!). Defaults to False.
app.jinja_env.lstrip_blocks = True  # If this is set to True leading spaces and tabs are stripped from the start of a line to a block. Defaults to False.

user = {
    "username": "Grey Li",
    "bio": "A boy who loves movies and music.",
}

movies = [
    {"name": "My Neighbor Totoro", "year": "1988"},
    {"name": "Three Colours trilogy", "year": "1993"},
    {"name": "Forrest Gump", "year": "1994"},
    {"name": "Perfect Blue", "year": "1997"},
    {"name": "The Matrix", "year": "1999"},
    {"name": "Memento", "year": "2000"},
    {"name": "The Bucket list", "year": "2007"},
    {"name": "Black Swan", "year": "2010"},
    {"name": "Gone Girl", "year": "2014"},
    {"name": "CoCo", "year": "2017"},
]


@app.route("/watchlist")
def watchlist():
    return render_template("watchlist.html", user=user, movies=movies)


@app.route("/")
def index():
    return render_template("index.html")


# register template context handler
@app.context_processor
def inject_info():
    foo = "I am foo."
    return dict(foo=foo)  # equal to: return {'foo': foo}


# register template global function
@app.template_global()
def bar():
    return "I am bar."


# register template filter
@app.template_filter()
def musical(s):
    return s + Markup(" &#9835;")


# register template test
@app.template_test()
def baz(n):
    if n == "baz":
        return True
    return False


@app.route("/watchlist2")
def watchlist_with_static():
    return render_template("watchlist_with_static.html", user=user, movies=movies)


# message flashing
@app.route("/flash")
def just_flash():
    flash("哈哈哈 Flash消息")  # 可以通过get_flashed_messages()获得消息
    return redirect(url_for("index"))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500
