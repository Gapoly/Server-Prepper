# Config general

import os
import sys
import subprocess

def title ():

    print(r"""
.·:''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''':·.
: :   ____                             ____                                   : :
: :  / ___|  ___ _ ____   _____ _ __  |  _ \ _ __ ___ _ __  _ __   ___ _ __   : :
: :  \___ \ / _ \ '__\ \ / / _ \ '__| | |_) | '__/ _ \ '_ \| '_ \ / _ \ '__|  : :
: :   ___) |  __/ |   \ V /  __/ |    |  __/| | |  __/ |_) | |_) |  __/ |     : :
: :  |____/ \___|_|    \_/ \___|_|    |_|   |_|  \___| .__/| .__/ \___|_|     : :
: :                                                  |_|   |_|                : :
'·:...........................................................................:·'
""")


def pre_install ():
    print("Lancement des mises à jours")
    os.system("sudo apt-get update > /dev/null 2>&1")
    print("Installation des packages nécessaires")
    os.system("sudo apt-get install ufw openssl -y > /dev/null 2>&1")

def check_root ():
  
    if os.geteuid() == 0:
        print("Utilisateur Root détecté - Le script continue")

    # Récupération du nom d'utilisateur
    user = os.getenv("USER", "unknown")
    
    try:
        # Vérification si l'utilisateur fait partie du groupe sudo
        groups = subprocess.check_output(["groups", user], text=True).strip().split()
        if "sudo" in groups:
            print("Vous êtes dans le groupe sudo.")
            print("Veuillez entrer votre mot de passe pour continuer.")
            
            # Vérification du mot de passe sudo
            try:
                subprocess.check_call(["sudo", "-v"])
                print("Mot de passe accepté. Le script continue.")
                #sys.exit(0)
            except subprocess.CalledProcessError:
                print("Mot de passe incorrect. Le script s'arrête.")
                #sys.exit(1)
        else:
            print("Vous n'avez pas les permissions nécessaires pour exécuter ce script.")
            #sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la vérification des permissions : {e}")
        #sys.exit(1)