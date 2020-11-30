import os
import shutil
from random import *

liste_fichiers = []
liste_fichiers_finale = []
dicti = {}
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
                if element[1][1:] not in dicti.keys():
                    dicti[element[1][1:]] = [element[0]]
                # not new type
                else:
                    dicti[element[1][1:]].append(element[0])
        # not repertory
        else:
            element = os.path.splitext(i)
            if element[1][1:] not in dicti.keys():
                dicti[element[1][1:]] = [element[0]]
            else:
                dicti[element[1][1:]].append(element[0])
    return dicti


def grouper_fichiers():
    recuperer_fichiers()
    try:
        for i in dicti.keys():
            if os.path.isdir("D:\\Téléchargements\\" + i):
                pass
            else:
                if i == "":
                    os.mkdir("D:\\Téléchargements\\Autres")
                # Probleme avec deux .exe differents (.exe et .EXE)
                elif i == ".EXE":
                    pass
                elif i != "":
                    os.mkdir("D:\\Téléchargements\\" + i)
    except Exception as e:
        print(e)


def deplacer_fichiers():
    recuperer_fichiers()
    grouper_fichiers()
    for cle, value in dicti.items():
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
            numb = str(randint(0, 1_000_000))
            os.renames("D:\\Téléchargements\\" + element[0] + "." + element[1][1:],
                       "D:\\Téléchargements\\" + element[0] + "(" + numb + ")" + "." + element[1][1:])
            shutil.move("D:\\Téléchargements\\" + element[0] + "(" + numb + ")." + element[1][1:],
                        "D:\\Téléchargements\\" + element[1][1:])
        else:
            if i == "z":
                os.remove("D:\\Téléchargements\\z")
            elif i not in dicti.keys():
                shutil.move("D:\\Téléchargements\\" + i,
                            "D:\\Téléchargements\\Autres")


def demander_type(demand):
    grouper_fichiers()
    try:
        result = os.listdir("D:\\Téléchargements\\" + demand)
        return result
    except Exception as e:
        return e


def recuperer_type():
    for i in recuperer_fichiers().keys():
        ext.append(i)
    return ext


def fichier_en_forme(demand):
    fichiers_ext = ""
    for i in demander_type(demand):
        fichiers_ext += i + "\n"
    return fichiers_ext


continu = "Oui"
choix_console = input("Voulez_vous travailler exclusivement en console ? (Oui/Non) ")

if choix_console == "Oui" or choix_console == "oui":

    print("Sélectionner ce que vous voulez faire parmis ces propositions :")
    print("1) 'Récupérer fichiers' afin de récupérer tous les fichiers présents dans votre dossier"
          " de téléchargements")
    print("2) 'Grouper fichiers' afin de créer tous les sous-dossiers de votre dossier de téléchargements")
    print("3) 'Déplacer fichiers' afin de déplacer tous les fichiers de votre dossier de téléchargement dans son "
          "sous-dossier")
    print("4) 'Demander type' afin de récupérer tous les fichiers d'un certain type")
    print("5) 'Récupérer type' afin de récupérer tous les types de fichiers")

    while continu == "Oui" or continu == "oui":
        choix = input("Que voulez faire ? ")

        if choix == "Récuperer fichiers" or choix == "récuperer fichiers":
            print("Voici tous vos fichiers présents dans votre dossier de téléchargements et ses sous-dossiers : ")
            print(recuperer_fichiers())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "Grouper fichiers" or choix == "grouper fichiers":
            grouper_fichiers()
            print("Les sous-dossiers viennent de se créer dans votre dossier de téléchargements")
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "Déplacer fichiers" or choix == "déplacer fichiers":
            deplacer_fichiers()
            print("Tous vos fichiers viennent de se trier dans leur sous-dossier respectif")
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "Demander type" or choix == "demander type":
            type_ext = input("Quel type de fichier voulez-vous récupérer ? ")
            print("Voici vos fichiers {}".format(type_ext))
            print(demander_type(type_ext))
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "Récupérer type" or choix == "récupérer type":
            print("Voici tous les types de fichier présents dans votre dossier de téléchargements : ")
            print(recuperer_type())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")
        else:
            print("Veuillez entrer un choix disponible ")

else:
    print("Alors vous pouvez ouvrir l'interface graphique.")

# librairie shh1 et md5 (moins bien (sécurisée))
