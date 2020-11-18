from tkinter import *
import tkinter.ttk as ttk
from libs.fonct import *
from database import *

# Mise à jour

deplacer_fichiers()

# Configuration

window = Tk()
window.title("Trouve Tout")
window.geometry("720x480")
window.minsize(1000, 800)
window.config(background="#F94747")
frame = Frame(window, bg="#F94747")


# Functions
def apparaitre_fich_spec():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(1000, 800)
    top.config(background="#F94747")
    lab = Label(top, text="Fenêtre de listing de \n fichiers specifiques", font=("Arial", 20), bg="#F94747", fg="white")
    liste = ttk.Combobox(top, values=recuperer_type())

    def mettre_a_jour():
        remplir_table_infos()
        remplir_Table_Comparaison()
        a = liste.get()
        lab = Label(top, text=fichier_en_forme(a))
        lab.pack()

        """lab.config(text=fichier_en_forme(a))"""

    button = Button(top, text="Afficher les dossiers", command=mettre_a_jour)
    liste.pack()
    button.pack()
    lab.pack(expand=YES)


def apparaitre_compa():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(1000, 800)
    top.config(background="#F94747")
    lab = Label(top, text="Evolution fichiers de téléchargements", font=("Arial", 24), bg="#F94747", fg="white")
    lab.pack()
    explication = Label(top, text="Vous allez entrer une date minimum qui comparera l'évolution \n de votre dossier "
                                  "de téléchargements de cette date à aujourd'hui.", font=("Arial", 20),
                        bg="#F94747", fg="white")
    explication.pack()
    entry = Label(top, text="Veuillez entrer une date sous la forme : yyyy-mm-dd", font=("Arial", 14),
                  bg="#F94747", fg="white")
    entry.pack()
    value = Entry(top)
    value.focus_set()
    value.pack()

    def show():
        remplir_table_infos()
        remplir_Table_Comparaison()
        date = value.get()
        result = Label(top, text=result_comparaison(date))
        result.pack()

    validation = Button(top, text="Valider Date Max", command=show)
    validation.pack()


# Main page
label_title = Label(window, text="Bienvenue sur notre Trouve Tout", font=("Arial", 40), bg="#F94747", fg="white")
label_title.pack(expand=YES)

list_button = Button(frame, text="Lister Fichiers Spécifiques", bg="white", fg="#F94747",
                     command=apparaitre_fich_spec)

comparaison_button = Button(frame, text="Voir évolution", bg="white", fg="#F94747", command=apparaitre_compa)

list_button.pack()
comparaison_button.pack()
frame.pack(expand=YES)

window.mainloop()
