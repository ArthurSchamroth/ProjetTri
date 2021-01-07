from libs.fonct import *
from libs.classes import *
import unittest


class TestDescription(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Description("PDF"), Description)
        self.assertEqual(Description("PDF").ajouter_description(), "Voici vos fichiers PDF ainsi qu'une brève "
                                                                   "description : format Adobe Acrobat. Protégez"
                                                                   " le style et évitez les modifications.")
        self.assertRaises(TypeError, Description, 1)


class TestFichier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Fichier("Test", "pdf"), Fichier)
        self.assertEqual(Fichier("Test", "pdf").demande_type(), "pdf")
        self.assertEqual(Fichier("Test", "pdf").fichier_en_forme(), "Test.pdf")
        self.assertRaises(TypeError, Fichier, 1, 1)


class TestDossier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Dossier("Test"), Dossier)


class FonctionTest(unittest.TestCase):
    def recup_fichier_test(self):
        self.assertEqual(recuperer_fichiers(), 
)

