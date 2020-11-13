from tkinter import *

# Configurer l'interface graphique

window = Tk()

window.title("Trouve Tout")
window.geometry("720x480")
window.minsize(800, 600)

window.config(background="#F94747")

frame = Frame(window, bg="#F94747")

def apparaitre_fich_spec():
    top = Toplevel(window)
    top.title("Trouve Tout")
    top.geometry("720x480")
    top.minsize(1280, 600)

    top.config(background="#F94747")

    lab = Label(top, text="Fenetre de listing de fichiers specifiques", font=("Arial", 40), bg="#F94747", fg="white")
    lab.pack(expand=YES)


# Informations dans interface
label_title = Label(window, text="Bienvenue sur notre Trouve Tout", font=("Arial", 40), bg="#F94747", fg="white")
label_title.pack(expand=YES)

afficher_list_button = Button(frame, text="Lister Fichiers Spécifiques", bg="white", fg="#F94747",
                              command=apparaitre_fich_spec)
afficher_list_button.pack()

frame.pack(expand=YES)

# Afficher interface graphique
window.mainloop()
