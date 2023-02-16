import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session


app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    return render_template("index.html")
