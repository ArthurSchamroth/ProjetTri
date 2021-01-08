from tkinter import *
import tkinter.ttk as ttk
#from database import *
from libs.fonct import *
from libs.classe_dossier import *

# Mise à jour

deplacer_fichiers()


# Main page
def commencer():
    global window
    window = Tk()
    window.title("Trouve Tout")
    window.geometry("720x480")
    window.minsize(720, 480)
    window.config(background="#C6A5A5")
    label_title = Label(window, text="Bienvenue sur notre \n Trouve Tout", font=("Arial", 40), bg="#C6A5A5", fg="white")
    label_title.place(relx=0.5, rely=0.2, anchor=CENTER)

    list_button = Button(window, text="Lister Fichiers Spécifiques", bg="white", fg="#C6A5A5",
                         command=apparaitre_fich_spec, width=30, pady=5)

    comparaison_button = Button(window, text="Voir Evolution", bg="white", fg="#C6A5A5", command=apparaitre_compa,
                                width=30, pady=5)

    ouvrir_appli_button = Button(window, text="Ouvrir Appli", bg="white", fg="#C6A5A5", command=apparaitre_ouvrir,
                                 width=30, pady=5)

    list_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    comparaison_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    ouvrir_appli_button.place(relx=0.5, rely=0.7, anchor=CENTER)
    window.mainloop()


# Functions
def apparaitre_fich_spec():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(720, 480)
    top.config(background="#C6A5A5")
    titre = Label(top, text="Fenêtre de listing de \n fichiers specifiques", font=("Arial", 20), bg="#C6A5A5",
                  fg="white")
    liste = ttk.Combobox(top, values=recuperer_type())
    liste.place(relx=0.4, rely=0.2, anchor=CENTER)
    lab = Text(top, font=("Arial", 12), bg="#C6A5A5", fg="white", relief=FLAT)

    def mettre_a_jour():
        remplir_table_infos()
        remplir_Table_Comparaison()
        a = liste.get()
        lab.delete(1.0, END)
        lab.insert(1.0, Dossier(a).fichier_en_forme())
        lab.place(relx=0.5, rely=0.7, anchor=CENTER)

    button = Button(top, text="Afficher les dossiers", command=mettre_a_jour)
    button.place(relx=0.6, rely=0.2, anchor=CENTER)
    titre.place(relx=0.5, rely=0.1, anchor=CENTER)
    lab.config(highlightbackground="#C6A5A5")


def apparaitre_compa():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(720, 480)
    top.config(background="#C6A5A5")
    lab = Label(top, text="Evolution fichiers de téléchargements", font=("Arial", 24), bg="#C6A5A5", fg="white")
    lab.place(relx=0.5, rely=0.1, anchor=CENTER)
    explication = Label(top, text="Veuillez sélectionner une date, vous obtiendrez ensuite le nombre\n "
                                  "de nouveaux téléchargements vous avez effectué depuis ce jour.", font=("Arial", 15),
                        bg="#C6A5A5", fg="white")
    explication.place(relx=0.5, rely=0.2, anchor=CENTER)
    liste = ttk.Combobox(top, values=recuperer_date())
    result = StringVar()
    result.set("C'est ici que s'affichera le résultat")
    lab = Label(top, textvariable=result, font=("Arial", 12), bg="#C6A5A5", fg="white")

    def show():
        remplir_table_infos()
        remplir_Table_Comparaison()
        date = liste.get()
        result.set(result_comparaison(date))

    liste.place(relx=0.4, rely=0.3, anchor=CENTER)
    validation = Button(top, text="Valider Date Max", command=show)
    validation.place(relx=0.6, rely=0.3, anchor=CENTER)
    lab.place(relx=0.5, rely=0.5, anchor=CENTER)


def apparaitre_ouvrir():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(720, 480)
    top.config(background="#C6A5A5")
    lab = Label(top, text="Lancement fichier", font=("Arial", 24), bg="#C6A5A5", fg="white")
    lab.place(relx=0.5, rely=0.1, anchor=CENTER)
    explication = Label(top, text="Veuillez commencer par sélectionner un type de fichier\n"
                                  "Ensuite veuillez sélectionner un fichier, exécutable ou autre que vous auriez "
                                  "sélectionné", font=("Arial", 15),
                        bg="#C6A5A5", fg="white")
    explication.place(relx=0.5, rely=0.2, anchor=CENTER)
    liste = ttk.Combobox(top, values=recuperer_type())
    liste.place(relx=0.4, rely=0.4, anchor=CENTER)
    confirmation_txt = StringVar()
    confirmation = Label(top, textvariable=confirmation_txt, font=("Arial", 12), bg="#C6A5A5", fg="white")
    confirmation.place(relx=0.6, rely=0.9, anchor=CENTER)

    def choix_fichier():
        type = liste.get()
        liste_fichiers = ttk.Combobox(top, values=Dossier(type).demander_type())
        liste_fichiers.place(relx=0.4, rely=0.55, anchor=CENTER)

        def lancer_recherche():
            fichier = liste_fichiers.get()
            fichier_complet = str(fichier + "." + type)
            Fichier(fichier, type).recherche()
            confirmation_txt.set("Le fichier {} s'est ouvert dans Google Chrome".format(fichier))
        button_fichier = Button(top, text="Valider Fichier", command=lancer_recherche)
        button_fichier.place(relx=0.6, rely=0.55, anchor=CENTER)

    validation_type = Button(top, text="Valider Type", command=choix_fichier)
    validation_type.place(relx=0.6, rely=0.4, anchor=CENTER)
