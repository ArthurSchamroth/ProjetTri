from libs.fonct import fonct_console
from libs.interf_graph import commencer


choix_console = input("Voulez_vous travailler exclusivement en console ? (Oui/Non) ")

if choix_console == "Oui" or choix_console == "oui":
    fonct_console()
else:
    commencer()
    # Quand on tape 'Non' ca doit lancer l'interface graphique
