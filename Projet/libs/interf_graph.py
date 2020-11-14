from tkinter import *
import tkinter.ttk as ttk
from libs.fonct import *

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
    scrollbar = Scrollbar(lab)
    scrollbar.pack(side=RIGHT, fill=Y)
    o = ttk.Combobox(top, values=recuperer_type())
    def mettre_a_jour():
        a = o.get()
        liste = Listbox(lab, yscrollcommand=scrollbar.set)
        for i in demander_type(a):
            liste.insert(END, i)
        liste.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=liste.yview)
        """lab.config(text=fichier_en_forme(a))"""
    button = Button(top, text="Afficher les dossiers", command=mettre_a_jour)
    o.pack()
    button.pack()
    lab.pack(expand=YES)


# Main page
label_title = Label(window, text="Bienvenue sur notre Trouve Tout", font=("Arial", 40), bg="#F94747", fg="white")
label_title.pack(expand=YES)

afficher_list_button = Button(frame, text="Lister Fichiers Spécifiques", bg="white", fg="#F94747",
                              command=apparaitre_fich_spec)
afficher_list_button.pack()
frame.pack(expand=YES)


window.mainloop()
