from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():

    marks = {
        "Gauttam": 90,
        "Robert" : 70,
        "victory": 66,
        "Ronaldo": 50,
        "Tina" : 100
    }

    values = [1,marks,67]
    return jsonify(values)

app.run(debug=True)