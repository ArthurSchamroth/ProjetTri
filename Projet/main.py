from libs.fonct import fonct_console

choix_console = input("Voulez_vous travailler exclusivement en console ? (Oui/Non) ")

if choix_console == "Oui" or choix_console == "oui":
    fonct_console()
else:
    print("coucou")
    # Quand on tape 'Non' ca doit lancer l'interface graphique
