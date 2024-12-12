#!/bin/bash

# Récupérer le nom de l'utilisateur actuel
user=$(whoami)




# Vérifier si l'utilisateur est root

check_root () {

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