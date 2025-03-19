import mysql.connector

# Class Utilisateur
class Utilisateur:
    def __init__(self, hote, utilisateur, motdepasse, bdd):
        self.hote = hote
        self.utilisateur = utilisateur
        self.motdepasse = motdepasse
        self.bdd = bdd

    def connect(self):
        self.bd = mysql.connector.connect(
            host = self.hote,
            user = self.utilisateur,
            password = self.motdepasse,
            database = self.bdd
        )
        self.cursor = self.bd.cursor()

    def close(self):
        self.cursor.close()
        self.bd.close()

    def ajout(self, nom, prenom, email, motdepasse):
        self.connect()
        ajout_req = f'insert into utilisateur (nom, prenom, email, mot_de_passe) \
            \nvalues ("{nom}", "{prenom}", "{email}", "{motdepasse}")'
       
        self.cursor.execute(ajout_req)

        self.bd.commit()
        self.close()

    def lecture(self):
        self.connect()
        lecture_req = f"select * from utilisateur"
        self.cursor.execute(lecture_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition(self, condition):
        self.connect()
        lecture_cond_req = f"select * from utilisateur where {condition}"
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition_mdp(self, condition):
        self.connect()
        lecture_cond_req = f'select mot_de_passe from utilisateur where {condition}'
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchone()[0]
        print(resultat)
        self.close()
        return resultat

    def maj(self, nouvelle_valeur, condition):
        self.connect()
        maj_req = f'update utilisateur set mot_de_passe = "{nouvelle_valeur}" where email = "{condition}"'
        self.cursor.execute(maj_req)
        self.bd.commit()
        self.close()

    def supr(self, condition):
        self.connect()
        supr_req = f"delete from utilisateur where {condition}"
        self.cursor.execute(supr_req)
        self.bd.commit()
        self.close()
    
    def verif_email(self, email):
        self.connect()
        req = f'select * from utilisateur where email = "{email}"'
        self.cursor.execute(req)
        result = self.cursor.fetchone()
        if result != None:
            return False
        else:
            return True
        self.close()