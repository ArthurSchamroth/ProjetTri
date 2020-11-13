import os
import shutil
from random import *

liste_fichiers = []
liste_fichiers_finale = []
dict = {}
dossiers = []


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
        for i in dict.keys():
            if i == "":
                os.mkdir("D:\\Téléchargements\\Autres")
            # Probleme avec deux .exe differents (.exe et .EXE)
            elif i == ".EXE":
                pass
            elif i != "":
                os.mkdir("D:\\Téléchargements\\" + i[1:])
    except:
        pass


def deplacer_fichiers():
    recuperer_fichiers()
    grouper_fichiers()
    for cle, value in dict.items():
        for i in value:
            if (str(i) + "." + str(cle)) in os.listdir("D:\\Téléchargements\\" + cle):
                pass
            else:
                shutil.move("D:\\Téléchargements\\" + i + "." + cle,
                            "D:\\Téléchargements\\" + cle + "\\" + i + "." + cle)
    for i in os.listdir("D:\\Téléchargements"):
        if not os.path.isdir("D:\\Téléchargements\\" + i):
            element = os.path.splitext(i)
            chiffre = str(randint(0, 1_000_000))
            os.renames("D:\\Téléchargements\\" + element[0] + "." + element[1][1:],
                       "D:\\Téléchargements\\" + element[0] + "(" + chiffre + ")" + "." + element[1][1:])
            shutil.move("D:\\Téléchargements\\" + element[0] + "(" + chiffre + ")." + element[1][1:],
                        "D:\\Téléchargements\\" + element[1][1:])
            print(element)


def demander_type():
    grouper_fichiers()
    try:
        demand = input("Veuillez entrer l'extension des fichiers que vous désirez : ")
        result = os.listdir("D:\\Téléchargements\\" + demand)
        return result
    except:
        return "Type d'extension inconnue (ex : 'pdf', pas '.pdf')"


print(deplacer_fichiers())
