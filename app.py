from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def homepage():
    return "<p>homepage!</p>"

@app.route("/first")
def return_first():
    return render_template("first.html")

@app.route("/second")
def return_second():
    return render_template("second.html")

