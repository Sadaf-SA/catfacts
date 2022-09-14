from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url).json()["fact"]
    return response


@app.route("/")
def index():
    fact = get_fact()
    return render_template("index.html", quote = fact)



app.run(debug=false, host='0.0.0.0')
