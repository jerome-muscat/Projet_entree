import string, hashlib, json

# try:
#     with open("mdp.json", "r") as f:
#         dict_mot_de_passe = json.load(f)

# except:
#     dict_mot_de_passe = {}

def verif_mdp(mdp):
    while True:
        lettre_miniscule = 0
        lettre_majuscule = 0
        nombre_caractere = 0
        chiffres = 0
        caractere_speciaux = "! @ # $ % ^ & *"

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

def saisi_mdp():
    while True:
        mdp = input("Veuillez saisir mot_de_passe nouveau mot de passe : ")
        verif = verif_mdp(mdp)
        if verif != "Valide":
            print(verif)
        else:
            print("Mot de passe valide")
            crypte = hashlib.sha256(mdp.encode()).hexdigest()
            return crypte

# nom = input("Veuillez entrer votre nom d'utilisateur : ")
mot_de_passe = saisi_mdp()
# if nom in dict_mot_de_passe:
#     if mot_de_passe in dict_mot_de_passe[nom]:
#         print("Mot de passe déjà existants !")
#     elif mot_de_passe not in dict_mot_de_passe[nom]:
#         dict_mot_de_passe[nom] += [mot_de_passe]
#         print("Mot de passe ajouté au fichier historique")
# else: 
#     dict_mot_de_passe[nom] = [mot_de_passe]
#     print("Mot de passe ajouté au fichier historique")
    
# affich_mot_de_passe = input("Voulez vous afficher tous vos mots de passe ? (oui ou non) ")
# if affich_mot_de_passe.lower() ==  "oui":
#     print(dict_mot_de_passe[nom])

# with open("mdp.json", "w") as f:
#     json.dump(dict_mot_de_passe, f, separators=(",", ": "), indent=4)
