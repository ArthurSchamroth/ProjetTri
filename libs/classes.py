from libs.extensions import *
import os

# Chemin non importable depuis fonct.py
chemin_repertoire = input("Veuillez entrer le chemin absolu de votre dossier de téléchargements en doublant vos "
                          "\\ (exemple: D:\\\\Téléchargements) ")


class Description:
    def __init__(self, typ: str):
        """

        :param typ: str: type dont il faut récupérer la description
        """
        if type(typ) != str:
            raise TypeError("Paramètre doit être un string")
        else:
            self.type = typ
            if typ in dictionnaire_extensions:
                self.description = dictionnaire_extensions[typ]
            else:
                self.description = "Type de fichier invalide !"

    def ajouter_description(self) -> str:
        """

        :return: str: présentation de la description
        """
        if self.type in dictionnaire_extensions:
            return str("Voici vos fichiers {} ainsi qu'une brève description : {}".format(self.type, self.description))
        else:
            return str("Le type d'extension {} nous est inconnu !".format(self.type))


class Fichier:
    def __init__(self, nom: str, exte: str):
        """

        :param nom: str: nom du fichier
        :param exte: str: extension du fichier
        """
        if type(nom) != str and type(exte) != str:
            raise TypeError("Paramètres doivent être des string")
        else:
            self.nom = nom
            self.ext = exte
            self.ext_recherchable = False

    def demande_type(self) -> str:
        """

        :return: str: extension du fichier
        """
        return str(self.ext[1:])

    def fichier_en_forme(self) -> str:
        """

        :return: str: nom du fichier avec son extension
        """
        return str(self.nom + "." + self.ext)

    def recherche(self):
        """

        :return: str: string indiquant que ce type d'extension est recherchable ou non
        """
        if self.ext.upper() in dictionnaire_extensions_recherchable.keys():
            self.ext_recherchable = True
            print("Ce type de fichier est ouvrable sur Google Chrome !")
            if self.fichier_en_forme() in os.listdir(chemin_repertoire):
                choix = input("Voulez-vous ouvrir dans Google Chrome ? ")
                if choix == "Oui" or choix == "oui":
                    subprocess.Popen(("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", chemin_repertoire
                                      + "\\" + self.ext + "\\" + self.fichier_en_forme))
                    print("Le fichier s'est ouvert dans Google Chrome")
            else:
                print("Ce fichier n'existe pas !")

        else:
            print("Ce type de fichier n'est pas ouvrable sur Google Chrome !")


class Dossier:
    def __init__(self, name: str, contenu: list):
        """

        :param name: str: nom du dossier
        :param contenu: list: liste des différents du fichier du dossier
        """
        if type(name) != str and type(contenu) != list:
            raise TypeError("Paramètres doivent être un string et une liste")
        else:
            self.name = name
            self.contenu = contenu

    def ouvrir_dossier(self):
        result = ""
        for i in range(len(self.contenu) - 1):
            result += self.contenu[i] + ", "
        result += self.contenu[-1]
        return result

