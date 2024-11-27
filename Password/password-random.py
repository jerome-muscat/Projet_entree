import string, hashlib, json, random

try:
    with open("aleatoire.json", "r") as f:
        dict_mot_de_passe = json.load(f)

except:
    dict_mot_de_passe = {}


caracteres = "!@#$%^&*"
test = ""

def generation_mdp(caractere, caracteres, mdp):
    i = 0
    while i != caractere:
        lettre_miniscule = random.choice(string.ascii_lowercase)
        lettre_majuscule = random.choice(string.ascii_uppercase)
        chiffre = random.choice(string.digits)
        caractere_speciaux = random.choice(caracteres)
        mdp_aleatoire = random.choice((lettre_miniscule, lettre_majuscule, chiffre, caractere_speciaux))
        mdp += mdp_aleatoire
        i+=1
    return mdp

def verif_mdp(mdp, caractere_speciaux, caractere):
    while True:
        lettre_miniscule = 0
        lettre_majuscule = 0
        nombre_caractere = 0
        chiffres = 0

        if len(mdp) >= 8:
            for i in string.ascii_lowercase:
                if i in mdp :
                    lettre_miniscule += 1

            for x in string.ascii_uppercase:
                if x in mdp :
                    lettre_majuscule += 1
                    
            for y in string.digits:
                if y in mdp :
                    chiffres += 1

            for z in caractere_speciaux:
                if z in mdp :
                    nombre_caractere += 1            
            
            if lettre_miniscule > 0 and lettre_majuscule > 0 and nombre_caractere > 0 and chiffres > 0:
                return "Valide"
            
            else:
                return "Pas valide"

        else:
            return "Pas valide"

def choix_mdp():
    while True:
        caractere = int(input("Veuillez choisir un nombre de caractère : "))
        mdp = generation_mdp(caractere, caracteres, test)
        verif = verif_mdp(mdp, caracteres, caractere)
        if verif != "Valide":
            print(verif)
        else:
            print("Mot de passe valide")
            crypte = hashlib.sha256(mdp.encode()).hexdigest()
            return crypte

nom = input("Veuillez entrer votre nom d'utilisateur : ")
mot_de_passe = choix_mdp()
if nom in dict_mot_de_passe:
    if mot_de_passe in dict_mot_de_passe[nom]:
        print("Mot de passe déjà existants !")
    elif mot_de_passe not in dict_mot_de_passe[nom]:
        dict_mot_de_passe[nom] += [mot_de_passe]
        print("Mot de passe ajouté au fichier historique")
else: 
    dict_mot_de_passe[nom] = [mot_de_passe]
    print("Mot de passe ajouté au fichier historique")
    
affich_mot_de_passe = input("Voulez vous afficher tous vos mots de passe ? (oui ou non) ")
if affich_mot_de_passe.lower() ==  "oui":
    print(dict_mot_de_passe[nom])

with open("aleatoire.json", "w") as f:
    json.dump(dict_mot_de_passe, f, separators=(",", ": "), indent=4)