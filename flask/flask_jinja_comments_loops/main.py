from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():

    marks = {
        "marry":50,
        "john": 60,
        "victory":80,
        "Raj":70,
        "robert":90,
        "Kim":100,
        "Gauttam":11
    }
    return render_template("index.html",marks=marks)

app.run(debug=True)