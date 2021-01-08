from libs.variables import *
import os


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
