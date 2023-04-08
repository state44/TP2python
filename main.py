from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def fonction_page_bonjour():
    return render_template("formulaire.html")




@app.route("/submit_form")
def submit_form():
    var_prenom = request.args.get("prenom")
    var_nom = request.args.get("nom")
    var_numero = request.args.get("numero")
    var_anglais = request.args.get("anglais")
    var_math = request.args.get("math")
    var_francais = request.args.get("francais")
    var_science = request.args.get("science")
    var_histoire = request.args.get("histoire")
    
    with open("data.txt", "w") as file:
        # write data to file
        file.write(f"Prenom: {var_prenom}\n")
        file.write(f"Nom: {var_nom}\n")
        file.write(f"Numero etudiant: {var_numero}\n")
        file.write(f"Note en anglais: {var_anglais}\n")
        file.write(f"Note en math: {var_math}\n")
        file.write(f"Note en francais: {var_francais}\n")
        file.write(f"Note en sciences: {var_science}\n")
        file.write(f"Note en histoire: {var_histoire}\n")
        
        
    return render_template("submit_form.html", prenom=var_prenom, nom=var_nom, numero=var_numero, anglais=var_anglais, math=var_math, francais=var_francais, science=var_science, histoire=var_histoire)





if __name__ == '__main__':
    app.run()
