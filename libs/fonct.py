from libs.classes import *
import os
import shutil
from random import *
from libs.extensions import *
import subprocess
import hashlib

dicti = {}
dicti_objets = {}
dossiers = []
ext = []
fichiers_ext = ""

chemin_repertoire = input("Veuillez entrer le chemin absolu de votre dossier de téléchargements en doublant vos "
                          "\\ (exemple: D:\\\\Téléchargements) ")


def recuperer_fichiers():
    for i in os.listdir(chemin_repertoire):
        # repertory
        if os.path.isdir(chemin_repertoire + "\\" + i):
            for j in os.listdir(chemin_repertoire + "\\" + i):
                element = os.path.splitext(j)
                # new type
                if element[1][1:] not in dicti_objets.keys():
                    if element[1] == "":
                        dicti_objets["Dossier"] = [Fichier(element[0], element[1])]
                    else:
                        dicti_objets[element[1][1:]] = [Fichier(element[0], element[1])]
                # not new type
                else:
                    if element[1] == "":
                        dicti_objets["Dossier"].append(Fichier(element[0], element[1]))
                    else:
                        dicti_objets[element[1][1:]].append(Fichier(element[0], element[1]))
        # not repertory
        else:
            element = os.path.splitext(i)
            if element[1][1:] not in dicti_objets.keys():
                dicti_objets[element[1][1:]] = [Fichier(element[0], element[1])]
            else:
                dicti_objets[element[1][1:]].append(Fichier(element[0], element[1]))
    return dicti_objets


def afficher_fichiers_console():
    result = ""
    for i in recuperer_fichiers().keys():
        result += i + " : "
        for j in recuperer_fichiers()[i]:
            result += j.nom + ", "
        result += "\n"
    return result


def grouper_fichiers():
    recuperer_fichiers()
    try:
        for i in dicti.keys():
            if os.path.isdir(chemin_repertoire + "\\" + i):
                pass
            elif i == "":
                os.mkdir(chemin_repertoire + "\\FichierChelou")
            else:
                if i == "":
                    os.mkdir(chemin_repertoire + "\\Autres")
                # Probleme avec deux .exe differents (.exe et .EXE)
                elif i == ".EXE":
                    pass
                elif i != "":
                    os.mkdir(chemin_repertoire + "\\" + i)
    except Exception as e:
        print(e)


def deplacer_fichiers():
    recuperer_fichiers()
    grouper_fichiers()
    for i in os.listdir(chemin_repertoire):
        if not os.path.isdir(chemin_repertoire + "\\" + i):
            # if element is already in the correct file ==> rename this element with a number between 0 and 1 000 000.
            element = os.path.splitext(i)
            if element[1] == "":
                shutil.move(chemin_repertoire + "\\" + element[0] + "." + element[1][1:],
                            chemin_repertoire + "\\FichierChelou")
            else:
                nombre = str(randint(0, 1_000_000))
                os.renames(chemin_repertoire + "\\" + element[0] + "." + element[1][1:],
                           chemin_repertoire + "\\" + element[0] + "(" + nombre + ")" + "." + element[1][1:])
                shutil.move(chemin_repertoire + "\\" + element[0] + "(" + nombre + ")." + element[1][1:],
                            chemin_repertoire + "\\" + element[1][1:])
            """hash_element = hashlib.md5((chemin_repertoire + "\\" + i).encode("utf-8")).hexdigest()
            hash_elements_dossier = []
            for j in os.listdir(chemin_repertoire + "\\" + element[1][1:]):
                hash_elements_dossier.append(j)
            for j in range(len(hash_elements_dossier)):
                hash_elements_dossier[j] = hashlib.md5(hash_elements_dossier[j].encode("utf-8")).hexdigest()
            if hash_element in hash_elements_dossier:
                print("Ok")"""

        else:
            if i == "z":
                os.remove(chemin_repertoire + "\\z")
            elif i not in dicti_objets.keys():
                shutil.move(chemin_repertoire + "\\" + i,
                            chemin_repertoire + "\\Autres")


def demander_type(demande):
    grouper_fichiers()
    # Utilisation liste comprehension
    if demande in dicti_objets.keys():
        resultat = os.listdir(chemin_repertoire + "\\" + demande)
        result = [os.path.splitext(x)[0] for x in resultat]
        return result
    else:
        return "Vous n'avez pas de sous dossier du type {}".format(demande)


def recuperer_type():
    for i in recuperer_fichiers().keys():
        if i != "":
            ext.append(i)
    return ext


def fichier_en_forme(demande):
    fichiers_ext = ""
    for i in demander_type(demande):
        fichiers_ext += i + "\n"
    return fichiers_ext


def ajouter_description(demande):
    return Description(demande.upper()).ajouter_description()


def ouverture_appli(fichier):
    fichier = os.path.splitext(fichier)
    subprocess.Popen(("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                      chemin_repertoire + "\\" + fichier[1][1:] + "\\" + str(fichier[0] + fichier[1])))


def recherche_internet(fichier: str):
    fichier = os.path.splitext(fichier)
    if str(fichier[0] + fichier[1]) in os.listdir(chemin_repertoire + "\\" + fichier[1][1:]):
        element = RechercheInternet(fichier[0], fichier[1])
        print(element.recherche())
        if element.ext_recherchable:
            choix = input("Voulez l'ouvir dans Google Chrome ? ")
            if choix == "Oui" or choix == "oui":
                subprocess.Popen(("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                                  chemin_repertoire + "\\" + fichier[1][1:] + "\\" + str(fichier[0] + fichier[1])))
    else:
        return "Ce fichier n'existe pas !"


def fonct_console():
    continu = "Oui"
    print("Sélectionner un numéro de propositions :")
    print("1) 'Récupérer fichiers' afin de récupérer tous les fichiers présents dans votre dossier"
          " de téléchargements")
    print("2) 'Demander type' afin de récupérer tous les fichiers d'un certain type")
    print("3) 'Récupérer type' afin de récupérer tous les types de fichiers")
    print("4) 'Ouvrir fichier' afin d'ouvrir un fichier dans Google Chrome")

    while continu == "Oui" or continu == "oui":
        choix = input("Que voulez faire ? ")

        if choix == "1":
            print("Voici tous vos fichiers présents dans votre dossier de téléchargements et ses sous-dossiers avec "
                  "leur type d'extension: ")
            print(afficher_fichiers_console())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "2":
            type_ext = input("Quel type de fichier voulez-vous récupérer ? ")
            print(ajouter_description(type_ext))
            print(demander_type(type_ext))
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "3":
            print("Voici tous les types de fichier présents dans votre dossier de téléchargements : ")
            print(recuperer_type())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")
        elif choix == "4":
            type_ext = input("Quel type de fichier voulez-vous ouvrir ? ")
            print("Voici les fichiers que vous pouvez ouvrir de ce type : {}".format(demander_type(type_ext)))
            fichier_a_ouvrir = input("Quel fichier voulez vous ouvrir ? ")
            recherche_internet(str(fichier_a_ouvrir + "." + type_ext))
            print("Le fichier s'est ouvert dans Google Chrome")
        else:
            print("Veuillez entrer un choix disponible, attention de ne pas ajouter un espace à la fin de votre "
                  "choix.")

    else:
        print("Veuillez lancer l'interface graphique")


# librairie shh1 et md5 (moins bien (sécurisée))

print(fonct_console())