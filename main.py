from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def fonction_page_bonjour():
    return render_template("formulaire.html")

if __name__ == '__main__':
    app.run()
