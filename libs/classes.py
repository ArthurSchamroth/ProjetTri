from libs.extensions import *


class Description:
    def __init__(self, typ: str):
        """

        :param typ: str
        """
        self.description = dictionnaire_extensions[typ]

    def ajouter_description(self) -> str:
        """

        :return: str
        """
        return str(self.description)


class Titre:
    def __init__(self, nom: str, ext: str):
        """

        :param nom: str: nom de "Titr"
        :param ext: str: extension de "Titre"
        """
        self.nom = nom
        self.ext = ext


class RechercheInternet(Titre):
    def __init__(self, nom: str, ext: str):
        """

        :param nom: str: nom du titre qui sera peut etre cherchable sur internet
        :param ext: str: extension du titre qui sera peut etre cherchable sur internet
        """
        super().__init__(nom, ext)
        self.ext_recherchable = False

    def recherche(self):
        """

        :return: str: string indiquant que ce type d'extension est recherchable ou non
        """
        if self.ext_recherchable in dictionnaire_extensions_recherchable:
            self.ext_recherchable = True
            return "Ce fichier est recherchable sur internet !"
        else:
            return "Ce fichier n'est pas recherchable sur internet !"


class Fichier:
    def __init__(self, nom: str, exte: str):
        """

        :param nom: str: nom du fichier
        :param exte: str: extension du fichier
        """
        self.nom = nom
        self.ext = exte

    def demande_type(self) -> str:
        """

        :return: str: extension du fichier
        """
        return str(self.ext[1:])

    def fichier_en_forme(self) -> str:
        """

        :return: str: nom du fichier avec son extension
        """
        return str(self.nom + self.ext)


class Dossier:
    def __init__(self, name: str, contenu: list):
        """

        :param name: str: nom du dossier
        :param contenu: list: liste des différents du fichier du dossier
        """
        self.name = name
        self.contenu = contenu
