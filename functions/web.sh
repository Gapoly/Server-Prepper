#!/bin/bash

web_install() {
    echo "Installation d'Apache2"
    sudo apt-get install apache2 -y > /dev/null 2>&1

    echo "Voulez-vous installer PHP et ses dépendances ? [y/n]"
    read php_choice

    while true; do
        if [ "$php_choice" == "y" or "Y" ]; then
            echo "Installation de PHP et de ses dépendances..."
            sudo apt-get install php curl php-curl -y > /dev/null 2>&1
            break
        elif [ "$php_choice" == "n" or "N" ]; then
            echo "Installation de PHP annulée."
            break
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read php_choice
        fi
    done
}
