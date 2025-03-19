# Projet d'Admission à Epitech  

Bienvenue dans mon projet présenté pour mon admission à **Epitech**. Ce projet est une fusion de diverses fonctionnalités issues de trois de mes précédents projets : **[gestion_de_stock](https://github.com/jerome-muscat/gestion_de_stock)**, **[myDiscord](https://github.com/jerome-muscat/myDiscord)** et **[Password](https://github.com/jerome-muscat/Password)**.  

## Fonctionnalités  

### 🔐 Gestion des Comptes et de l'Authentification  
- **Création de compte sécurisée** avec validation des champs **nom, prénom et email** via des expressions régulières (**regex**).  
- **Vérification avancée du mot de passe** :
  - L'utilisateur doit saisir son mot de passe **deux fois** pour éviter toute erreur de saisie.
  - Une fonction contrôle ensuite sa **complexité** :
    - Minimum **12 caractères**.
    - Présence d'au moins **une lettre minuscule**, **une lettre majuscule**, **un chiffre** et **un caractère spécial**.
    - Conformité avec les **normes de sécurité actuelles**.
- **Génération automatique d'un mot de passe sécurisé à la demande** lors de la création du compte ou de la réinitialisation du mot de passe.
- **Authentification sécurisée** avec validation des identifiants selon les formats attendus.  

### 📦 Gestion des Produits  
- **Ajout d'un produit** en cliquant sur `Ajouter un produit`.  
- **Modification d'un produit** en cliquant sur `Modifier` dans la ligne correspondante.  
- **Suppression d'un produit** en cliquant sur `Effacer` dans la ligne correspondante.  

### 🏷️ Gestion des Catégories  
- Gestion des catégories en cliquant sur `Ajouter/Supprimer une catégorie`.  
- Dans la fenêtre de gestion des catégories, vous pourrez :  
  - **Ajouter une catégorie** en la saisissant dans le champ dédié et en cliquant sur `Valider`.  
  - **Modifier une catégorie** en cliquant sur `Modifier` dans la ligne correspondante.  
  - **Supprimer une catégorie** en cliquant sur `Effacer` dans la ligne correspondante.  