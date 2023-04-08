## Albert State
## 2046464
## TP2
############################################

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

####################formulaire pour rentrer les notes et les noms des etudiants####################

@app.route("/")
def fonction_page_bonjour():
    return render_template("formulaire.html")


####################tableau de bord pour afficher les noms des etudiants####################
####################Le tableau de bord gere aussi l'ecriture dans le fichier####################

@app.route("/tableauDeBord")
def tableauDeBord():
####################ecriture dans le fichier####################
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
    
    
####################lecture du fichier####################
    emplacement = "data.txt"
    f = open(emplacement, "r")
    file = f.readlines()
    
    noms = []
    
    for line in file:    
        if "Nom" in line:
            nom = line.split('Nom: ')[1].strip()
            noms.append(nom)

    return render_template("tableauDeBord.html", noms=noms)



#################### afficher les notes d'un etudiant selectionné a partir du tableau de bord ####################

@app.route("/afficherNotes", methods=["POST"])
def afficherNotes():
    
    nom = request.form.get("nom")
    
    emplacement = "data.txt"
    f = open(emplacement, "r")
    file = f.readlines()
    
    notes = {}
#################### lecture du fichier et recherche de l'information utile ####################
    
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
