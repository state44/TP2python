from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)



@app.route("/")
def fonction_page_bonjour():
    return render_template("formulaire.html")




@app.route("/submit_form")
def ecriture():
    var_prenom = request.args.get("prenom")
    var_nom = request.args.get("nom")
    var_numero = request.args.get("numero")
    var_anglais = request.args.get("anglais")
    var_math = request.args.get("math")
    var_francais = request.args.get("francais")
    var_sciences = request.args.get("sciences")
    var_histoire = request.args.get("histoire")
    
    emplacement = "data.txt"
    
    f = open(emplacement, "a")
    f.write(f"Prenom: {var_prenom}\n")
    f.write(f"Nom: {var_nom}\n")
    f.write(f"Numero etudiant: {var_numero}\n")
    f.write(f"Notes de l'etudiant: {var_anglais}, {var_math}, {var_francais}, {var_sciences}, {var_histoire}\n")

        
        
    return render_template("tableauDeBord.html", prenom=var_prenom, nom=var_nom, numero=var_numero, anglais=var_anglais, math=var_math, francais=var_francais, sciences=var_sciences, histoire=var_histoire)

@app.route("/tableauDeBord")
def tableauDeBord():
    
    var_prenom = request.args.get("prenom")
    var_nom = request.args.get("nom")
    var_numero = request.args.get("numero")
    var_anglais = request.args.get("anglais")
    var_math = request.args.get("math")
    var_francais = request.args.get("francais")
    var_sciences = request.args.get("sciences")
    var_histoire = request.args.get("histoire")
    
    emplacement = "data.txt"
    
    f = open(emplacement, "a")
    f.write(f"Prenom: {var_prenom}\n")
    f.write(f"Nom: {var_nom}\n")
    f.write(f"Numero etudiant: {var_numero}\n")
    f.write(f"Notes de l'etudiant: {var_anglais}, {var_math}, {var_francais}, {var_sciences}, {var_histoire}\n")
    
    
    
    emplacement = "data.txt"
    f = open(emplacement, "r")
    file = f.readlines()
    
    noms = []
    
    for line in file:    
        if "Nom" in line:
            nom = line.split('Nom: ')[1].strip()
            noms.append(nom)

    return render_template("tableauDeBord.html", noms=noms)


@app.route("/afficherNotes", methods=["POST"])
def afficherNotes():
    
    nom = request.form.get("nom")
    
    emplacement = "data.txt"
    f = open(emplacement, "r")
    file = f.readlines()
    
    notes = {}
    
    for i in range(len(file)):
        if "Nom: " + nom in file[i]:
            prenom = file[i-1].split('Prenom: ')[1].strip()
            nomfamille = file[i].split('Nom: ')[1].strip()
            numeroetuidant = file[i+1].split('Numero etudiant: ')[1].strip()
            notes["prenom"] = prenom
            note_str = file[i+2].split(": ")[-1].strip()
            note_list = note_str.split(", ")
            for i in range(len(note_list)):
                notes[f"note{i+1}"] = note_list[i]

    return render_template("afficherNotes.html", notes=notes, nomfamille = nomfamille, numeroetuidant = numeroetuidant)



if __name__ == '__main__':
    app.run()
