#!/bin/bash

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