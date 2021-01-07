from libs.classes import *
import os
import shutil
from random import *
import hashlib

dicti = {}
dicti_objets = {}
dossiers = []
ext = []
fichiers_ext = ""


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
        tableau_dossier = []
        result += str(i) + " : "
        for j in recuperer_fichiers()[i]:
            if j.nom not in tableau_dossier:
                tableau_dossier.append(j.nom)
        for j in range(len(tableau_dossier) - 1):
            result += tableau_dossier[j] + ", "
        result += tableau_dossier[-1] + "\n"
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
        # ajouter comme
        print(e)


def recuperer_hash():
    tableau_hash = {}
    for i in recuperer_fichiers().keys():
        tableau_hash[i] = []
        if i == "Dossier":
            pass
        else:
            for j in recuperer_fichiers()[i]:
                nom = j.nom
                ext = j.ext
                nom_a_hasher = "b" + nom + ext
                hash_object = hashlib.sha256(str(nom_a_hasher).encode("utf-8"))
                final = hash_object.hexdigest()
                if final in tableau_hash[i]:
                    pass
                else:
                    tableau_hash[i].append(final)
    return tableau_hash


def deplacer_fichiers():
    recuperer_fichiers()
    grouper_fichiers()
    for i in os.listdir(chemin_repertoire):
        if not os.path.isdir(chemin_repertoire + "\\" + i):
            # if element is already in the correct file ==> rename this element with a number between 0 and 1 000 000.
            if i == "FichierChelou":
                pass
            else:
                element = os.path.splitext(i)
                nom_a_hasher = "b" + i
                hash_object = hashlib.sha256(str(nom_a_hasher).encode("utf-8"))
                if str(hash_object.hexdigest()) in recuperer_hash()[element[1][1:]]:
                    nombre = str(randint(0, 1_000_000))
                    os.renames(chemin_repertoire + "\\" + element[0] + "." + element[1][1:],
                               chemin_repertoire + "\\" + element[0] + "(" + nombre + ")" + "." + element[1][1:])
                    shutil.move(chemin_repertoire + "\\" + element[0] + "(" + nombre + ")." + element[1][1:],
                                chemin_repertoire + "\\" + element[1][1:])
                elif element[1] == "":
                    shutil.move(chemin_repertoire + "\\" + element[0] + "." + element[1][1:],
                                chemin_repertoire + "\\FichierChelou")
                else:
                    shutil.move(chemin_repertoire + "\\" + element[0] + element[1],
                                chemin_repertoire + "\\" + element[1][1:])

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


def fonct_console():
    continu = "Oui"
    print("Sélectionner un numéro de propositions :")
    print("1) 'Récupérer fichiers' afin de récupérer tous les fichiers présents dans votre dossier"
          " de téléchargements")
    print("2) 'Demander type' afin de récupérer tous les fichiers d'un certain type")
    print("3) 'Récupérer type' afin de récupérer tous les types de fichiers")
    print("4) 'Ouvrir fichier' afin d'ouvrir un fichier dans Google Chrome")
    print("Exit pour quiter le programe")

    while continu == "Oui" or continu == "oui":
        choix = input("Que voulez faire ? ")

        if choix == "1":
            print("Voici tous vos fichiers présents dans votre dossier de téléchargements et ses sous-dossiers avec "
                  "leur type d'extension: ")
            print(afficher_fichiers_console())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "2":
            type_ext = input("Quel type de fichier voulez-vous récupérer ? ")
            print(Description(type_ext).ajouter_description())
            print(demander_type(type_ext))
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "3":
            print("Voici tous les types de fichier présents dans votre dossier de téléchargements : ")
            print(recuperer_type())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "4":
            type_ext = input("Quel type de fichier voulez-vous ouvrir ? ")
            if type_ext in dicti_objets.keys():
                if type_ext.upper() in dictionnaire_extensions_recherchable.keys():
                    print("Voici les fichiers de ce type que vous pouvez ouvrir : {}".format(demander_type(type_ext)))
                    fichier_choisi = input("Veuillez sélectionner un fichier à ouvrir : ")
                    fichier_choisi = os.path.splitext(fichier_choisi)
                    fichier = Fichier(fichier_choisi[0], type_ext)
                    print(fichier.recherche())

                else:
                    print("Vous possèdez ce type de fichier, il n'est cependant pas ouvrable dans Google Chrome !")

            else:
                print("Vous ne possèdez pas de fichier de ce type !")

            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "exit" or choix == "Exit":
            print("Sortie interface....")
            exit()

        else:
            print("Veuillez entrer un choix disponible, attention de ne pas ajouter un espace à la fin de votre "
                  "choix.")

    else:
        print("Sortie du mode console...")
