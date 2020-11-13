import sqlite3
import datetime




def creer_Table_Infos():
    baseDeDonnees = sqlite3.connect("infos")
    curseur = baseDeDonnees.cursor()
    curseur.execute("create TABLE Infos (date ,nom TEXT NOT NULL, type NOT NULL)")
    baseDeDonnees.commit()


def creer_Table_Comparaison():
    baseDeDonnees = sqlite3.connect("infos.db")
    curseur = baseDeDonnees.cursor()
    curseur.execute("create TABLE Comparaison (date ,total INTEGER)")
    baseDeDonnees.commit()


def remplir_table_infos():
    baseDeDonnees = sqlite3.connect(r"C:\Users\scham\OneDrive - EPHEC asbl\BAC2\Q1\Développement Informatique II Pratique\Projet\libs\infos.db")
    curseur = baseDeDonnees.cursor()
    for cle, valeur in dict.items():
        for i in valeur:
            curseur.execute("INSERT INTO Infos VALUES(:date, :nom, :cle)",
                            {
                            "date": datetime.datetime.today().strftime('%Y-%m-%d'),
                            "nom": i,
                            "cle": cle
            })
    baseDeDonnees.commit()

def compter():
    total = 0
    baseDeDonnees = sqlite3.connect(r"C:\Users\scham\OneDrive - EPHEC asbl\BAC2\Q1\Développement Informatique II Pratique\Projet\libs\infos.db")
    curseur = baseDeDonnees.cursor()
    curseur.execute("select distinct nom from Infos")
    for i in curseur:
        total += 1
    return total


def remplir_Table_Comparaison():
    baseDeDonnees = sqlite3.connect(r"C:\Users\scham\OneDrive - EPHEC asbl\BAC2\Q1\Développement Informatique II Pratique\Projet\libs\infos.db")
    curseur = baseDeDonnees.cursor()
    curseur.execute("insert into Comparaison values(:date, :total)",
                    {
                        "date": datetime.datetime.today(),
                        "total": compter()
                    })
    baseDeDonnees.commit()


def comparaison():
    baseDeDonnees = sqlite3.connect(r"C:\Users\scham\OneDrive - EPHEC asbl\BAC2\Q1\Développement Informatique II Pratique\Projet\libs\infos.db")
    curseur = baseDeDonnees.cursor()
    curseur.execute("select nom, type from Infos where date < ?", (datetime.datetime.today(),))
    for i in curseur.fetchall():
        print(i)
    baseDeDonnees.commit()



print(creer_Table_Infos())