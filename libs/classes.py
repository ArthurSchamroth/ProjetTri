from libs.extensions import *
from libs.variables import *
import os
import subprocess
import hashlib


class Description:
    def __init__(self, typ: str):
        """

        :param typ: str: type dont il faut récupérer la description
        """
        if type(typ) != str:
            raise TypeError("Paramètre doit être un string")
        else:
            self.type = typ
            if typ.upper() in dictionnaire_extensions:
                self.description = dictionnaire_extensions[typ.upper()]
            else:
                self.description = "Type de fichier invalide !"

    def ajouter_description(self) -> str:
        """

        :return: str: présentation de la description
        """
        if self.type.upper() in dictionnaire_extensions:
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

    def ext_is_recherchable(self) -> bool:
        """

        :return: bool: True si ce type de fichier est recherchable
        """
        if self.ext.upper() in dictionnaire_extensions_recherchable.keys():
            self.ext_recherchable = True
        return True

    def recherche(self) -> str:
        """

        :return: str: string indiquant que ce type d'extension est recherchable ou non
        """
        if self.ext_is_recherchable():
            if self.fichier_en_forme() in os.listdir(chemin_repertoire + "\\" + self.ext):
                subprocess.Popen(("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", chemin_repertoire
                                  + "\\" + self.ext + "\\" + self.fichier_en_forme()))
                return "Le fichier s'est ouvert dans Google Chrome"
            else:
                return "Ce fichier n'existe pas !"

        else:
            return "Ce type de fichier n'est pas ouvrable sur Google Chrome !"

    def hash_fichier(self) -> str:
        """

        :return: str: hash du fichier
        """
        hashage = "b" + self.nom + self.ext
        hash_object = hashlib.sha256(str(hashage).encode("utf-8"))
        return hash_object.hexdigest()


class Dossier:
    def __init__(self, name: str) -> None:
        """

        :param name: str: nom du dossier
        """
        if type(name) != str:
            raise TypeError("Paramètres doivent être un string et une liste")
        else:
            self.name = name

    def demander_type(self) -> str or list:
        # Utilisation liste comprehension
        if self.name in dicti_objets.keys():
            resultat = os.listdir(chemin_repertoire + "\\" + self.name)
            result = [os.path.splitext(x)[0] for x in resultat]
            return result
        else:
            return "Vous n'avez pas de sous dossier du type {}".format(self.name)

    def fichier_en_forme(self) -> str:
        fichiers_ext = ""
        for i in self.demander_type():
            fichiers_ext += i + "\n"
        return fichiers_ext
