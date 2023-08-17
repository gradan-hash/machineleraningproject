from flask import Flask, request, render_template
import numpy as numpy
import pandas as pd

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

# create route for homepage


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prediction", methods=["POST,GET"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
      
    else:
      pass
