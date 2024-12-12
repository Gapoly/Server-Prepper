#!/usr/bin/python

# Fonctions publiques
import os
import subprocess
import time

# Sources Python
from conf.detection import sys_detec


# Lancement du script

subprocess.run(['bash', '-c', 'source ./conf/general.sh && welcome'])
print("")

print("Démarrage du script")
print("")

time.sleep(2.0)
print(sys_detec())
print("")

subprocess.run(['bash', '-c', 'source ./conf/general.sh && check_root'])

print(f"Mise à jour de votre système {host_executer}")
subprocess.run(['bash', '-c', 'source ./conf/general.sh && sys_update'])