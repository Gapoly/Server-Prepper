#!/usr/bin/python

# Fonctions publiques
import os
import subprocess
import time

# Les sources  Python
from conf.detection import sys_detec

# Les sources Bash



# Lancement du script

subprocess.call ("./conf/intro.sh",shell=True)
print("")

print("Démarrage du script")
print("")

time.sleep(2.0)
print(sys_detec())
