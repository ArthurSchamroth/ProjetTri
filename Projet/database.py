import mysql
from mysql import connector
from libs.fonct import *
import datetime

cnx = mysql.connector.connect(user="root", password="admin", host="127.0.0.1", database="infos")
db_name = "infos"
tables = {}
mycursor = cnx.cursor()
dict = recuperer_fichiers()


def creer_Table_Infos():
    mycursor.execute("CREATE TABLE Infos (id int primary key not null auto_increment,"
                     " Date date, Nom varchar(255), Type char(255))")


def creer_Table_Comparaison():
    mycursor.execute("CREATE TABLE Comparaison (id int primary key not null auto_increment,"
                     " Date date, Total Integer(100))")


def remplir_table_infos():
    print(dict.items())
    sqlFormula = "INSERT INTO Infos (Date, Nom, Type) VALUES (%s, %s, %s)"
    for cle, value in dict.items():
        for i in value:
            information = (datetime.datetime.today().strftime('%Y-%m-%d'), i, cle)
            mycursor.execute(sqlFormula, information)
    cnx.commit()


def remplir_Table_Comparaison():
    sqlFormula = "INSERT INTO Comparaison (Date, Total) VALUES(%s, %s)"
    information = (datetime.datetime.today().strftime('%Y-%m-%d'), compter())
    mycursor.execute(sqlFormula, information)
    cnx.commit()


def compter():
    total = 0
    mycursor.execute("select distinct nom from Infos")
    for i in mycursor.fetchall():
        total += 1
    return total


def comparaison(date):
    # Voir si pas possible de mettre deux dates, une de début et une de fin de comparaison
    mycursor.execute('SELECT Max(Total) FROM comparaison WHERE Date LIKE \'%' + date + '%\'')
    return mycursor.fetchone()


def result_comparaison(date):
    mycursor.execute('SELECT Max(Total) FROM comparaison WHERE Date LIKE Date(Now())')
    total_today = mycursor.fetchone()[0]
    difference = total_today - comparaison(date)[0]
    return "Depuis le {}, vous avez téléchargé {} nouveaux fichier(s)".format(date, difference)
