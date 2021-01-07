from libs.fonct import *


def fonct_console():
    grouper_fichiers()
    deplacer_fichiers()
    continu = "Oui"
    print("Sélectionner un numéro de propositions :")
    print("1) 'Récupérer fichiers' afin de récupérer tous les fichiers présents dans votre dossier"
          " de téléchargements")
    print("2) 'Demander type' afin de récupérer tous les fichiers d'un certain type")
    print("3) 'Récupérer type' afin de récupérer tous les types de fichiers")
    print("4) 'Ouvrir fichier' afin d'ouvrir un fichier dans Google Chrome")
    print("Exit pour quiter le programe")

    while continu == "Oui" or continu == "oui":
        choix = input("Que voulez faire ? ")

        if choix == "1":
            print("Voici tous vos fichiers présents dans votre dossier de téléchargements et ses sous-dossiers avec "
                  "leur type d'extension: ")
            print(afficher_fichiers_console())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "2":
            type_ext = input("Quel type de fichier voulez-vous récupérer ? ")
            print(Description(type_ext).ajouter_description())
            print(Dossier(type_ext).demander_type())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "3":
            print("Voici tous les types de fichier présents dans votre dossier de téléchargements : ")
            print(recuperer_type())
            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "4":
            type_ext = input("Quel type de fichier voulez-vous ouvrir ? ")
            if type_ext in dicti_objets.keys():
                if type_ext.upper() in dictionnaire_extensions_recherchable.keys():
                    print("Voici les fichiers de ce type que vous pouvez ouvrir : {}".
                          format(Dossier(type_ext).demander_type()))
                    fichier_choisi = input("Veuillez sélectionner un fichier à ouvrir : ")
                    fichier_choisi = os.path.splitext(fichier_choisi)
                    fichier = Fichier(fichier_choisi[0], type_ext)
                    print(fichier.recherche())

                else:
                    print("Vous possèdez ce type de fichier, il n'est cependant pas ouvrable dans Google Chrome !")

            else:
                print("Vous ne possèdez pas de fichier de ce type !")

            continu = input("Voulez-vous continuer à travailler en console ? (Oui/Non) ")

        elif choix == "exit" or choix == "Exit":
            print("Sortie interface....")
            exit()

        else:
            print("Veuillez entrer un choix disponible, attention de ne pas ajouter un espace à la fin de votre "
                  "choix.")

    else:
        print("Sortie du mode console...")