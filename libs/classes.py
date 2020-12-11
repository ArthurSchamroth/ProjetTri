import webbrowser
import os
from libs.extensions import *


class Description:
    def __init__(self, typ: str):
        self.description = dictionnaire_extensions[typ]

    def ajouter_description(self) -> str:
        return str(self.description)


class Titre:
    def __init__(self, nom: str, ext: str):
        self.nom = nom
        self.ext = ext


class RechercheInternet(Titre):
    def __init__(self, nom, ext, ext_recherchable=""):
        super().__init__(nom, ext)
        self.ext_recherchable = ext_recherchable

    def recherche(self):
        if self.ext_recherchable in dictionnaire_extensions_recherchable:
            return "Ce fichier est recherchable sur internet !"


class Fichier:
    def __init__(self, nom: str, exte: str):
        self.nom = nom
        self.ext = exte

    def demande_type(self) -> str:
        return str(self.ext[1:])

    def fichier_en_forme(self) -> str:
        return str(self.nom + self.ext)


class Dossier:
    def __init__(self, name: str, contenu: list):
        self.name = name
        self.contenu = contenu
