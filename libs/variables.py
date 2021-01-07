from winreg import *

dicti = {}
dicti_objets = {}
dossiers = []
ext = []
fichiers_ext = ""

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    chemin_repertoire = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
