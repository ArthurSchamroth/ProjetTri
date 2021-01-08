from libs.fonct import *
from libs.classe_fichier import *
from libs.classe_dossier import *
from libs.classe_description import *

import unittest


class TestDescription(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Description("PDF"), Description)
        self.assertEqual(Description("PDF").ajouter_description(), "Voici vos fichiers PDF ainsi qu'une brève "
                                                                   "description : format Adobe Acrobat. Protégez "
                                                                   "le style et évitez les modifications.")
        self.assertEqual(Description("abcd").ajouter_description(), "Le type d'extension abcd nous est inconnu !")
        self.assertRaises(TypeError, Description, 1)


class TestFichier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Fichier("Test", "pdf"), Fichier)
        self.assertEqual(Fichier("Test", "pdf").demande_type(), "pdf")
        self.assertEqual(Fichier("Test", "pdf").fichier_en_forme(), "Test.pdf")
        self.assertRaises(TypeError, Fichier, 1, 1)
        # self.assertEqual(Fichier("téléchargement", "jpg").recherche(), "Le fichier s'est ouvert dans Google Chrome")
        self.assertEqual(Fichier("test", "jpg").recherche(), "Ce fichier n'existe pas !")
        self.assertEqual(Fichier("noel flantier", "jpg").hash_fichier(),
                         "de1d6fe27533b4ba5cb75412b6c79a8139652134d010373953df1341e1b7eff8")


class TestDossier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Dossier("Test"), Dossier)
        self.assertRaises(TypeError, Dossier, 1)
        self.assertEqual(Dossier("lol").demander_type(), "Vous n'avez pas de sous dossier du type lol")


class TestFonct(unittest.TestCase):

    def setUp(self) -> None:
        global chemin_repertoire
        chemin_repertoire = str(os.path.abspath(os.path.dirname(__file__)) + "\\fichier_test")

    def test1(self):
        print(afficher_fichiers_console(chemin_repertoire))
        self.assertEqual(str(recuperer_type(chemin_repertoire)), "['aup', 'jpg', 'png']")
        self.assertEqual(str(recuperer_hash(chemin_repertoire)), "{'aup': ['37df9ea31c25b02e41d8569079bc3ee988bc9d667f0de5fffc7365978d22db5e'], 'jpg': ['013fb13cdd9bd083107bf356f7b36c665af6a563c1e0b7fd7236134fb0ed58dc'], 'png': ['f9c81708e487ef1e1038cb2db9329850d55000e2b2315228080769bacbe98b27']}")
        self.assertEqual(str(afficher_fichiers_console(chemin_repertoire)), "aup : bruit kaamelott\njpg : noel flantier\npng : pack(67611)\n")