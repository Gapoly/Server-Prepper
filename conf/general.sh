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
    echo "Installation des mises à jours"
    sudo apt-get upgrade -fy && sudo apt-get install ufw -y > /dev/null 2>&1
}



check_root () {

    user=$(whoami)
    if [ "$user" == "root" ]; then
        echo "Utilisateur Root détecté - Le script continue"
        exit 0
    fi

# Vérifier si l'utilisateur appartient au groupe sudo
    if groups "$user" | grep -qw "sudo"; then
        echo "Vous êtes dans le groupe sudo."
        echo "Veuillez entrer votre mot de passe pour continuer."
    
    # Tester une commande sudo pour demander le mot de passe
        if sudo -v; then
            echo "Mot de passe accepté. Le script continue."
            # Placez le reste du script ici
            exit 0
        else
            echo "Mot de passe incorrect. Le script s'arrête."
            exit 1
        fi
    else
        # Si l'utilisateur n'est ni root ni dans le groupe sudo
        echo "Vous n'avez pas les permissions nécessaires pour exécuter ce script."
        exit 1
    fi
}