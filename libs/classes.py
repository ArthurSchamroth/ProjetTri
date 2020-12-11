from libs.extensions import *


class Description:
    def __init__(self, typ: str):
        """

        :param typ: str: type dont il faut récupérer la description
        """
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
        self.ext = ext
        self.ext_recherchable = False

    def recherche(self):
        """

        :return: str: string indiquant que ce type d'extension est recherchable ou non
        """
        if self.ext.upper()[1:] in dictionnaire_extensions_recherchable.keys():
            self.ext_recherchable = True
            return "Ce fichier est ouvrable sur Google Chrome !"
        else:
            return "Ce fichier n'est pas ouvrable sur Google Chrome !"


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
