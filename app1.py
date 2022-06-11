from flask import Flask, render_template, request
import joblib
from input_form import *

pipeline = joblib.load("./pipeline.sav")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/api", methods = ["POST"])
def get_input():

    input       = request.form
    query_title = input["Title"]
    query_text  = input["Text"]
    query       = get_all_query(query_title, query_text)
    #print(query)
    query       = clean_query(query)
    #print(query)
    pred        = pipeline.predict(query)
    print(pred)
    dic         = {1:"REAL", 0:"FAKE"}
    return render_template("result.html", result=dic[pred[0]])

if __name__ == "__main__":
    app.run(debug = True)
