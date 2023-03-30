from flask import Flask 
from flask import render_template
from flask import request

monapp = Flask(__name__)


@monapp.route("/")
def fonction_page_bonjour():
    return render_template("formulaire.html")
