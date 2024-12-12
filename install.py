#!/usr/bin/python

# Fonctions publiques
import os
import subprocess
import time

# Sources Python
from conf.detection import sys_detec
from conf.menu import menu


# Lancement du script

subprocess.run(['bash', '-c', 'source ./conf/general.sh && welcome'])
print("")

print("Démarrage du script")
print("")

time.sleep(2.0)
system_test=sys_detec()
print("")

#subprocess.run(['bash', '-c', 'source ./conf/general.sh && check_root'])

print(f"Mise à jour de votre système {system_test}")
#subprocess.run(['bash', '-c', 'source ./conf/general.sh && sys_update'])

maballs=os.getcwd()
print(maballs)

menu ()