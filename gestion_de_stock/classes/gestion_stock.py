import tkinter as tk
import tkinter.ttk as ttk
from .Categorie import Categorie
from .Produit import Produit
import tkinter.messagebox as messagebox

# Class Gestion_Stock
class Gestion_Stock:
    def __init__(self, root):
        self.categorie = Categorie('localhost', 'root', 'Jerome', 'boutique')
        self.produit = Produit('localhost', 'root', 'Jerome', 'boutique') 

        self.root = root
        self.root2 = None

        self.resultat = None

        self.frame = None 

        self.treeview = None

        self.lecture_categorie = self.categorie.lecture()

        self.modif_window = None

        self.treeview_categorie = None

    def affich_nom(self, resultat):
        for row in resultat:
            req = f"id = {row[5]}"

            categorie = self.categorie.lectureCondition(req)
            nom_categorie = ""
            # print(categorie)
            for lettre in str(categorie):
                if lettre not in "(),'{[]}":
                    nom_categorie += lettre
                    # print(nom_categorie)
            self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], nom_categorie, row[3], row[4], "Modifier", "Effacer"))

    def clique_colonne_produit(self, event):
        region = self.treeview.identify_region(event.x, event.y)
        if region == "cell":
            item_id = self.treeview.identify_row(event.y)
            column_id = self.treeview.identify_column(event.x)

            if column_id == "#6":
                # Clic sur la colonne "modifier"
                self.modifier_produit(item_id)
                
            elif column_id == "#7":
                # Clic sur la colonne "effacer"
                self.effacer_produit(item_id)

    def validation(self, item_id, name_entry, description_entry, price_entry, quantity_entry, modif_window):
        reponse = messagebox.askyesno("Modifier", "Voulez-vous vraiment modifier ce produit ?")
        if reponse:        
            id_produit = self.treeview.item(item_id, "text")
            values = [
                    name_entry.get(),
                    description_entry.get('1.0', 'end-1c'),
                    self.treeview.item(item_id, "values")[2],
                    price_entry.get(),
                    quantity_entry.get(),
                    "Modifier",
                    "Effacer"
                ]
            verif = False

            try:    
                self.produit.maj("nom", f'"{values[0]}"', f"id = {id_produit}")
                self.produit.maj("description", f'"{values[1]}"', f"id = {id_produit}")
                self.produit.maj("prix", values[3], f"id = {id_produit}")
                self.produit.maj("quantite", values[4], f"id = {id_produit}")
                messagebox.showinfo("Etat modification", "Modification effectuée avec succès !")
                verif = True
                
            except:
                messagebox.showinfo("Etat modification", "Modification echouée !") 
            
            if verif:
                self.treeview.item(item_id, values=values)
                modif_window.destroy()

    def ajout_valid(self, name_entry, description_entry, categorie_entry, price_entry, quantity_entry, modif_window):
        reponse = messagebox.askyesno("Ajout", "Voulez-vous vraiment ajouter ce produit ?")
        if reponse:
            values = [
                    name_entry.get(),
                    description_entry.get('1.0', 'end-1c'),
                    categorie_entry.get(),
                    price_entry.get(),
                    quantity_entry.get(),
                    "Modifier",
                    "Effacer"
                ]
            
            verif = False

            id_category = self.categorie.lectureCondition_id(values[2])

            try:
                self.produit.ajout(values[0], values[1], values[3], values[4], id_category)
                messagebox.showinfo("Etat ajout", "Ajout effectué avec succès !")
                verif = True
                
            except:
                messagebox.showinfo("Etat ajout", "Ajout echoué !")
            
            if verif:
                self.treeview.insert("", "end", values=values)
                modif_window.destroy()

    def modifier_produit(self, item_id):
        modif_window = tk.Toplevel(self.root)
        modif_window.title("Modifier la ligne")
        modif_window.geometry("800x400")

        name_label = tk.Label(modif_window, text="Entrez le nom du produit:")
        description_label = tk.Label(modif_window, text="Entrez la description du produit:")
        price_label = tk.Label(modif_window, text="Entrez le prix du produit:")
        quantity_label = tk.Label(modif_window, text="Entrez la quantité du produit:")

        name_var = tk.StringVar(value=self.treeview.item(item_id, "values")[0])
        description_var = tk.StringVar(value=self.treeview.item(item_id, "values")[1])
        price_var = tk.StringVar(value=self.treeview.item(item_id, "values")[3])
        quantity_var = tk.StringVar(value=self.treeview.item(item_id, "values")[4])

        name_entry = tk.Entry(modif_window, textvariable=name_var, width=100)
        description_entry = tk.Text(modif_window, height=5, width=90)
        description_entry.insert(tk.END, description_var.get())
        price_entry = tk.Entry(modif_window, textvariable=price_var, width=100)
        quantity_entry = tk.Entry(modif_window, textvariable=quantity_var, width=100)

        name_label.pack()
        name_entry.pack()

        description_label.pack()
        description_entry.pack()

        price_label.pack()
        price_entry.pack()
        
        quantity_label.pack()
        quantity_entry.pack()
        
        valider_button = tk.Button(modif_window, text="Valider", command= lambda: self.validation(item_id, name_entry, description_entry, price_entry, quantity_entry, modif_window))
        valider_button.pack()

    def effacer_produit(self, item_id):
        reponse = messagebox.askyesno("Effacer", "Voulez-vous vraiment effacer cet enregistrement ?")
        if reponse:
            id_produit = self.treeview.item(item_id, "text")
            verif = False

            try:
                self.produit.supr(f"id = {id_produit}")
                messagebox.showinfo("Etat suppression", "Suppression effectuée avec succès !")
                verif = True

            except:
                messagebox.showinfo("Etat suppression", "Suppression echouée !")
                
            if verif:
                self.treeview.delete(item_id)

    def ajout(self):
        modif_window = tk.Toplevel(self.root)
        modif_window.title("Modifier la ligne")
        modif_window.geometry("800x400")
        
        name_label = tk.Label(modif_window, text="Entrez le nom du produit:")
        description_label = tk.Label(modif_window, text="Entrez la description du produit:")
        categorie_label = tk.Label(modif_window, text="Entrez la catégorie du produit:")
        price_label = tk.Label(modif_window, text="Entrez le prix du produit:")
        quantity_label = tk.Label(modif_window, text="Entrez la quantité du produit:")

        name_entry = tk.Entry(modif_window, width=100)
        description_entry = tk.Text(modif_window, height=5, width=90)
        categorie_entry = tk.Entry(modif_window, width=100)
        price_entry = tk.Entry(modif_window, width=100)
        quantity_entry = tk.Entry(modif_window, width=100)

        name_label.pack()
        name_entry.pack()

        description_label.pack()
        description_entry.pack()

        categorie_label.pack()
        categorie_entry.pack()

        price_label.pack()
        price_entry.pack()
        
        quantity_label.pack()
        quantity_entry.pack()
            
        valider_button = tk.Button(modif_window, text="Valider", command=lambda: self.ajout_valid(name_entry, description_entry, categorie_entry, price_entry, quantity_entry, modif_window))
        valider_button.pack()  

    def validation_modif_categorie(self, item_id, name_entry):
        reponse = messagebox.askyesno("Modifier", "Voulez-vous vraiment modifier ce produit ?")
        if reponse:
            values = [
                    name_entry.get(),
                    "Modifier",
                    "Effacer"
                ]
            id_categorie = self.treeview_categorie.item(item_id, "text")
            verif = False

            try:
                self.categorie.maj("nom", f'"{values[0]}"', f"id = {id_categorie}")
                messagebox.showinfo("Etat modification", "Modification effectuée avec succès !")
                
                verif = True
                        
            except:
                messagebox.showinfo("Etat modification", "Modification echouée !") 

            if verif:
                self.modif_window.destroy()
                self.treeview_categorie.item(item_id, values=values)   

    def modifier_categorie(self, item_id):
        self.modif_window = tk.Toplevel(self.root)
        self.modif_window.title("Modifier la ligne")
        self.modif_window.geometry("800x400")

        name_label = tk.Label(self.modif_window, text="Entrez le nom du produit:")

        name_var = tk.StringVar(value=self.treeview_categorie.item(item_id, "values")[0])

        name_entry = tk.Entry(self.modif_window, textvariable=name_var, width=100)

        name_label.pack()
        name_entry.pack()
            
        valider_button = tk.Button(self.modif_window, text="Valider", command=lambda: self.validation_modif_categorie(item_id, name_entry))
        valider_button.pack()

    def effacer_categorie(self, item_id):
        reponse = messagebox.askyesno("Effacer", "Voulez-vous vraiment effacer cet enregistrement ?")
        if reponse:
            
            id_categorie = self.treeview_categorie.item(item_id, "text")

            try:
                self.produit.supr(f"id_categorie = {id_categorie}")
                self.categorie.supr(f"id = {id_categorie}")
                messagebox.showinfo("Etat suppression", "Suppression effectuée avec succès !")
                self.treeview_categorie.delete(item_id)

            except:
                messagebox.showinfo("Etat suppression", "Suppression echouée !")

    def clique_colonne_categorie(self, event):
        region = self.treeview_categorie.identify_region(event.x, event.y)
        if region == "cell":
            item_id = self.treeview_categorie.identify_row(event.y)
            column_id = self.treeview_categorie.identify_column(event.x)

            if column_id == "#2":
                # Clic sur la colonne "modifier"
                self.modifier_categorie(item_id)

            elif column_id == "#3":
                # Clic sur la colonne "effacer"
                self.effacer_categorie(item_id)

    def validation_ajout_categorie(self, name_entry):
        reponse = messagebox.askyesno("Ajouter", "Voulez-vous vraiment ajouter ce produit ?")
        if reponse:
            values = [
                    name_entry.get(),
                    "Modifier",
                    "Effacer"
                ]
            verif = False

            try:
                self.categorie.ajout(f"{values[0]}")
                messagebox.showinfo("Etat ajout", "Ajout effectuée avec succès !")
                verif = True

            except:
                messagebox.showinfo("Etat ajout", "Ajout echouée !") 

            if verif:
                self.modif_window.destroy()
                self.treeview_category.insert('', 'end', values=values)
                
    def ajout_categorie(self, categorie):
        self.modif_window = tk.Toplevel(self.root)
        self.modif_window.title("Modifier la ligne")
        self.modif_window.geometry("800x400")


        self.treeview_categorie = ttk.Treeview(self.modif_window, height=len(self.lecture_categorie))
        self.treeview_categorie.pack()

        self.treeview_categorie['columns'] = ('name', 'modifier', 'effacer')
        self.treeview_categorie.heading('#0', text='ID')
        self.treeview_categorie.column('#0', width=60)
        self.treeview_categorie.heading('name', text='Name')
        self.treeview_categorie.heading('modifier', text='Modifier')
        self.treeview_categorie.column('modifier', width=60)
        self.treeview_categorie.heading('effacer', text='Effacer')
        self.treeview_categorie.column('effacer', width=60)
        self.treeview_categorie.bind("<Button-1>", self.clique_colonne_categorie)

        nom_label = tk.Label(self.modif_window, text="Entrez le nom de la catégorie:")
        nom_entry = tk.Entry(self.modif_window, width=100)

        ajout_button = tk.Button(self.modif_window, text="Valider", command=lambda: self.validation_ajout_categorie(nom_entry))

        nom_label.pack()
        nom_entry.pack()
        ajout_button.pack()

        self.lecture_categorie = self.categorie.lecture()
        
        print(self.lecture_categorie)

        for row in categorie:
            nom_categorie = ""
            for lettre in str(row[1]):
                if lettre not in "(),'{[]}":
                    nom_categorie += lettre
            self.treeview_categorie.insert('', 'end', text=row[0], values=(nom_categorie, "Modifier", "Effacer"))

    def fenetre_gestion_stock(self):
        self.root2 = tk.Toplevel()
        self.root2.geometry("1000x700")
        self.root2.title("Gestion de stock")

        # self.resultat = self.produit.lecture()

        self.frame = tk.Frame(self.root2)

        self.frame.pack(pady=10)

        self.resultat = self.produit.lecture()

        self.treeview = ttk.Treeview(self.frame, height=len(self.resultat))
        self.treeview.pack(side=tk.LEFT) 

        self.treeview['columns'] = ('name', 'description', 'categorie', 'price', 'quantity', 'modifier', 'effacer')
        self.treeview.heading('#0', text='ID')
        self.treeview.column('#0', width=60)
        self.treeview.heading('name', text='Name')
        self.treeview.column('name', width=200)
        self.treeview.heading('description', text='Description')
        self.treeview.column('description', width=300)
        self.treeview.heading('categorie', text='Categorie')
        self.treeview.column('categorie', width=90)
        self.treeview.heading('price', text='Price')
        self.treeview.column('price', width=60, anchor=tk.CENTER)
        self.treeview.heading('quantity', text='Quantity')
        self.treeview.column('quantity', width=60)
        self.treeview.heading('modifier', text='Modifier')
        self.treeview.column('modifier', width=60)
        self.treeview.heading('effacer', text='Effacer')
        self.treeview.column('effacer', width=60)
        self.treeview.bind("<Button-1>", self.clique_colonne_produit)

        self.affich_nom(self.resultat)

        ajout_button = tk.Button(self.root2, text="Ajouter un produit", command=lambda: self.ajout())
        ajout_button.pack()

        self.lecture_categorie = self.categorie.lecture()

        ajout_button = tk.Button(self.root2, text="Ajouter/supprimer une catégorie", command=lambda: self.ajout_categorie(self.lecture_categorie))
        ajout_button.pack()