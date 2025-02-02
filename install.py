#!/usr/bin/python3

# Fonctions publiques
import os
import subprocess
import time

# Sources Python
from conf.detection import sys_detec
from conf.menu import menu
from conf.config import *

# Lancement du script

title()
print("")

time.sleep(1.0)
print("Démarrage du script")
print("")

time.sleep(2.0)
host=sys_detec()
print("")

check_root()

pre_install()

menu ()