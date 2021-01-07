from libs.fonct import *
import unittest
from libs.classes import *

"""
heritage, polymorphisme, surcharge operateur, pre, post, + dans les classes que dans les fonctions
"""


class TestDescription(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Description("PDF"), Description)
        self.assertEqual(Description("PDF").ajouter_description(), "Voici vos fichiers PDF ainsi qu'une brève "
                                                                   "description : format Adobe Acrobat. Protégez"
                                                                   " le style et évitez les modifications.")

    """def test2(self):
        self.assertRaises(TypeError, Description(1))"""


class TestTitre(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Titre("Test", ".pdf"), Titre)
        self.assertEqual((Titre("Test", ".txt").get_titre()), "Test")

    """def test2(self):
        self.assertRaises(TypeError, Titre(1, .3))"""


class TestRechercheInternet(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(RechercheInternet("Test", ".pdf"), RechercheInternet)
        self.assertEqual(RechercheInternet("Test", ".pdf").recherche(), "Ce type de fichier n'est pas ouvrable sur"

                                                                        " Google Chrome !")

    def test2(self):
        self.assertIsInstance(RechercheInternet("Test", "pdf"), RechercheInternet)
        self.assertEqual(RechercheInternet("Test", "pdf").recherche(), "Ce type de fichier est ouvrable sur"
                                                                       " Google Chrome !")


class TestFichier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Fichier("Test", ".pdf"), Fichier)
        self.assertEqual(Fichier("Test", ".pdf").demande_type(), "pdf")
        self.assertEqual(Fichier("Test", ".pdf").fichier_en_forme(), "Test.pdf")

    """def test2(self):
        self.assertRaises(TypeError, Fichier(1, 1))"""


class TestDossier(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(Dossier("Test", ["1", "2", "3"]), Dossier)
        self.assertEqual(Dossier("Test", ["1", "2", "3"]).ouvrir_dossier(), "1, 2, 3")

    def test2(self):
        self.assertIsInstance(Dossier(Titre("Test").get_titre(), [Fichier("elem1", ".txt").fichier_en_forme(),
                                                                  Fichier("elem2", ".txt").fichier_en_forme(),
                                                                  Fichier("elem3", ".txt").fichier_en_forme()
                                                                  ]), Dossier)
        self.assertEqual(Dossier(Titre("Test").get_titre(), [Fichier("elem1", ".txt").fichier_en_forme(),
                                                             Fichier("elem2", ".txt").fichier_en_forme(),
                                                             Fichier("elem3", ".txt").fichier_en_forme()
                                                             ]).ouvrir_dossier(), "elem1.txt, elem2.txt, elem3.txt")


class TestRecuperFichiersConsole(unittest.TestCase):
    # Chemin C:\Users\scham\OneDrive - EPHEC asbl\BAC2\Q1\Développement Informatique II Pratique\Projet w Github\dossier_testing1
    def test_recup_fichiers1(self):
        self.assertEqual(afficher_fichiers_console(), "mp4 : 1 Astable, 1 Bascule RS à NAND, "
                                                      "1 Démo Proteus\n"
                                                      "c : main(12246), main\n"
                                                      "csv : moodle(666914), moodle\n")
