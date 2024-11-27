from customtkinter import *
from tkinter import *

class LoginPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Page d'authentification")
        self.create_widgets()

    def create_widgets(self):
        self.label_username = Label(self.master, text="Nom d'utilisateur :")
        self.label_username.pack()
        self.entry_username = Entry(self.master)
        self.entry_username.pack()

        self.label_password = Label(self.master, text="Mot de passe :")
        self.label_password.pack()
        self.entry_password = Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_login = CTkButton(self.master, text="Se connecter", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "admin" and password == "password":
            print("Connexion réussie !")
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")

root = Tk()
app = LoginPage(master=root)
app.mainloop()
