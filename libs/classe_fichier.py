from libs.extensions import *
from libs.variables import *
import os
import subprocess
import hashlib


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
            self.hash = None

    def demande_type(self) -> str:
        """

        :return: str: extension du fichier
        """
        return str(self.ext)

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
        self.hash = hash_object.hexdigest()
        return hash_object.hexdigest()
    
    def __eq__(self, other) -> bool:
        """
        PRE:
            type(other) == Fichier
        POST:
            True if self.hash == other.hash
        RAISES:
            typeError if type(other) != Fichier
        """
        if type(other) != Fichier:
            raise TypeError
        else:
            return self.hash_fichier() == Fichier(other.nom, other.ext).hash_fichier()


