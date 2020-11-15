import os
import shutil
from random import *

liste_fichiers = []
liste_fichiers_finale = []
dict = {}
dossiers = []
ext = []
fichiers_ext = ""


def recuperer_fichiers():
    for i in os.listdir("D:\\Téléchargements"):
        # repertory
        if os.path.isdir("D:\\Téléchargements\\" + i):
            for j in os.listdir("D:\\Téléchargements\\" + i):
                element = os.path.splitext(j)
                # new type
                if element[1][1:] not in dict.keys():
                    dict[element[1][1:]] = [element[0]]
                # not new type
                else:
                    dict[element[1][1:]].append(element[0])
        # not repertory
        else:
            element = os.path.splitext(i)
            if element[1][1:] not in dict.keys():
                dict[element[1][1:]] = [element[0]]
            else:
                dict[element[1][1:]].append(element[0])
    return dict


def grouper_fichiers():
    recuperer_fichiers()
    try:
        print(dict.keys())
        for i in dict.keys():
            if i == "":
                os.mkdir("D:\\Téléchargements\\Autres")
            # Probleme avec deux .exe differents (.exe et .EXE)
            elif i == ".EXE":
                pass
            elif i != "":
                os.mkdir("D:\\Téléchargements\\" + i)
    except:
        pass


def deplacer_fichiers():
    recuperer_fichiers()
    grouper_fichiers()
    for cle, value in dict.items():
        if cle == "":
            pass
        else:
            for i in value:
                # if element is a directory ==> nothing
                if (str(i) + "." + str(cle)) in os.listdir("D:\\Téléchargements\\" + cle):
                    pass
                # if element is a file ==> move in the correct directory
                else:
                    shutil.move("D:\\Téléchargements\\" + i + "." + cle,
                                "D:\\Téléchargements\\" + cle + "\\" + i + "." + cle)

    for i in os.listdir("D:\\Téléchargements"):
        if not os.path.isdir("D:\\Téléchargements\\" + i):
            # if element is already in the correct file ==> rename this element with a number between 0 and 1 000 000.
            element = os.path.splitext(i)
            chiffre = str(randint(0, 1_000_000))
            os.renames("D:\\Téléchargements\\" + element[0] + "." + element[1][1:],
                       "D:\\Téléchargements\\" + element[0] + "(" + chiffre + ")" + "." + element[1][1:])
            shutil.move("D:\\Téléchargements\\" + element[0] + "(" + chiffre + ")." + element[1][1:],
                        "D:\\Téléchargements\\" + element[1][1:])
        else:
            if i == "z":
                os.remove("D:\\Téléchargements\\z")
            elif i not in dict.keys():
                shutil.move("D:\\Téléchargements\\" + i,
                            "D:\\Téléchargements\\Autres")


def demander_type(demand):
    grouper_fichiers()
    try:
        result = os.listdir("D:\\Téléchargements\\" + demand)
        return result
    except:
        return "Type d'extension inconnue"


def recuperer_type():
    for i in recuperer_fichiers().keys():
        ext.append(i)
    return ext


def fichier_en_forme(demand):
    fichiers_ext = ""
    for i in demander_type(demand):
        fichiers_ext += i + "\n"
    return fichiers_ext

