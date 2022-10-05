from flask import Flask
from flask import render_template


app = Flask(__name__,template_folder='src')

@app.route("/")
def hello():
    return render_template("app.html")
