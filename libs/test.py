from winreg import *

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

print(Downloads)