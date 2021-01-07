from libs.lancement_console import *
from libs.interf_graph import commencer

if __name__ == "__main__":
    choix_console = input("Voulez_vous travailler exclusivement en console ? (Oui/Non) ")

    if choix_console == "Oui" or choix_console == "oui":
        # Programme en console
        fonct_console()
    else:
        # Programme avec interface graphique
        commencer()
