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

time.sleep(1.0)
print("Démarrage du script")
print("")

time.sleep(2.0)
print(sys_detec()) 
print("")

subprocess.run(['bash', '-c', 'source ./conf/general.sh && check_root'])

subprocess.run(['bash', '-c', 'source ./conf/general.sh && sys_update'])

menu ()