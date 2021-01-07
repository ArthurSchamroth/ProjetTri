from libs.classes import *
import os
import shutil
from random import *
import hashlib


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
        raise e


def recuperer_hash():
    tableau_hash = {}
    for i in recuperer_fichiers().keys():
        tableau_hash[i] = []
        if i == "Dossier":
            pass
        else:
            for j in recuperer_fichiers()[i]:
                if Fichier(j.nom, j.ext).hash_fichier() in tableau_hash[i]:
                    pass
                else:
                    tableau_hash[i].append(Fichier(j.nom, j.ext).hash_fichier())
    return tableau_hash


def deplacer_fichiers():
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


def recuperer_type():
    for i in recuperer_fichiers().keys():
        if i != "":
            ext.append(i)
    return ext
