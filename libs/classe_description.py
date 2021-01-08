from libs.extensions import *


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