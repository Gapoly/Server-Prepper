# Config general

import os

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

