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

    while true; do
        echo ""

        cat << EOF
Quel port voulez vous ouvrir?

1. 80
2. 443
3. 80 & 443
4. Autre
EOF
        read web_port
        if [ "$web_port" == "1" ]; then
            echo "Ouverture du port 80"
            ufw allow 80
            break
        elif [ "$web_port"  == "2" ]; then
            echo "Ouverture du port 443"
            ufw allow 443
            break
        elif [ "$web_port"  == "3" ]; then
            echo "Ouverture du port 80 & 443"
            ufw allow 80
            ufw allow 443
            break
        elif [ "$web_port"  == "4" ]; then
            echo "Choisissez votre port"
            read custom_port
            ufw allow $custom_port
            break
        else;then
            echo "Valeur incorrect"
            continue
        fi
    done
}
