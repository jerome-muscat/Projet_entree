import string, hashlib, random

class Mot_de_passe:
    def __init__(self):
        pass
    
    def __verif_carectiriqtique_mdp(self, mdp):
        while True:
            lettre_miniscule = 0
            lettre_majuscule = 0
            nombre_caractere = 0
            chiffres = 0
            caractere_speciaux = "!@#$%^&*."

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

    def verif_mdp(self, mdp):
        verif = self.__verif_carectiriqtique_mdp(mdp)
        if verif != "Valide":
            return "Mot de passe non valide"
        else:
            crypte = hashlib.sha256(mdp.encode()).hexdigest()
            return crypte
        
    def generation():
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