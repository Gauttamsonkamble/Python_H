
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def hello_world():
    if (request.method == "POST"):
        #handle the form
        with open ("file.txt", "w") as f:
            f.write(f"The name is {request.form["name"]} and Email is {request.form["email"]}")
        return render_template("contacts.html")
    else:
        return render_template("contacts.html")


app.run(debug=True)