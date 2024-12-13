#!/bin/bash

welcome () {
cat << EOF
.·:''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''':·.
: :   ____                             ____                                   : :
: :  / ___|  ___ _ ____   _____ _ __  |  _ \ _ __ ___ _ __  _ __   ___ _ __   : :
: :  \___ \ / _ \ '__\ \ / / _ \ '__| | |_) | '__/ _ \ '_ \| '_ \ / _ \ '__|  : :
: :   ___) |  __/ |   \ V /  __/ |    |  __/| | |  __/ |_) | |_) |  __/ |     : :
: :  |____/ \___|_|    \_/ \___|_|    |_|   |_|  \___| .__/| .__/ \___|_|     : :
: :                                                  |_|   |_|                : :
'·:...........................................................................:·'
EOF
}

sys_update () {

    echo "Lancement des mises à jours"
    sudo apt-get update > /dev/null 2>&1
    echo "Installation des packages nécessaire"
    #sudo apt-get upgrade -y > /dev/null 2>&1
    sudo apt-get install ufw openssl -y > /dev/null 2>&1
}

check_root () {

    # Check root
    user=$(whoami)
    if [ "$user" == "root" ]; then
        echo "Utilisateur Root détecté - Le script continue"
        exit 0
    fi

    # Check Sudo
    if groups "$user" | grep -qw "sudo"; then
        echo "Vous êtes dans le groupe sudo."
        echo "Veuillez entrer votre mot de passe pour continuer."
    
        if sudo -v; then
            echo "Mot de passe accepté. Le script continue."
            exit 0
        else
            echo "Mot de passe incorrect. Le script s'arrête."
            exit 1
        fi
    else
        echo "Vous n'avez pas les permissions nécessaires pour exécuter ce script."
        exit 1
    fi
}