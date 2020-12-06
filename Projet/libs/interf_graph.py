from tkinter import *
import tkinter.ttk as ttk
from database import *
from libs.fonct import *

# Mise à jour

deplacer_fichiers()

# Configuration

window = Tk()
window.title("Trouve Tout")
window.geometry("720x480")
window.minsize(720, 480)
window.config(background="#C6A5A5")
frame = Frame(window, bg="#C6A5A5")


# Functions
def apparaitre_fich_spec():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(720, 480)
    top.config(background="#C6A5A5")
    titre = Label(top, text="Fenêtre de listing de \n fichiers specifiques", font=("Arial", 20), bg="#C6A5A5", fg="white")
    liste = ttk.Combobox(top, values=recuperer_type())
    liste.pack()
    lab = Text(top, font=("Arial", 12), bg="#C6A5A5", fg="white")

    def mettre_a_jour():
        remplir_table_infos()
        remplir_Table_Comparaison()
        a = liste.get()
        lab.delete(1.0, END)
        lab.insert(1.0, fichier_en_forme(a))
        lab.pack()

        """lab.config(text=fichier_en_forme(a))"""

    button = Button(top, text="Afficher les dossiers", command=mettre_a_jour)
    button.pack()
    titre.pack(expand=YES)
    lab.config(highlightbackground="#C6A5A5")
    lab.pack()


def apparaitre_compa():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(720, 480)
    top.config(background="#C6A5A5")
    lab = Label(top, text="Evolution fichiers de téléchargements", font=("Arial", 24), bg="#C6A5A5", fg="white")
    lab.pack()
    explication = Label(top, text="Veuillez sélectionner une date, vous obtiendrez ensuite le nombre\n "
                                  "de nouveaux téléchargements vous avez effectué depuis ce jour.", font=("Arial", 15),
                        bg="#C6A5A5", fg="white")
    explication.pack()
    liste = ttk.Combobox(top, values=recuperer_date())
    result = StringVar()
    result.set("C'est ici que s'affichera le résultat")
    lab = Label(top, textvariable=result, font=("Arial", 12), bg="#C6A5A5", fg="white")

    def show():
        remplir_table_infos()
        remplir_Table_Comparaison()
        date = liste.get()
        result.set(result_comparaison(date))

    liste.pack()
    validation = Button(top, text="Valider Date Max", command=show)
    validation.pack()
    lab.pack()


# Main page
label_title = Label(window, text="Bienvenue sur notre \n Trouve Tout", font=("Arial", 40), bg="#C6A5A5", fg="white")
label_title.pack(expand=YES)

list_button = Button(frame, text="Lister Fichiers Spécifiques", bg="white", fg="#C6A5A5",
                     command=apparaitre_fich_spec)

comparaison_button = Button(frame, text="Voir évolution", bg="white", fg="#C6A5A5", command=apparaitre_compa)

list_button.pack()
comparaison_button.pack()
frame.pack(expand=YES)

window.mainloop()
