#!/bin/bash

openssh_install () {

    echo "Installation de OpenSSH Server"
    sudo apt-get install openssh-server -y > /dev/null 2>&1

    echo "Voulez vous utiliser le port par défaut? [y/n]"
    read ssh_port

    while true; do
        if [ "$ssh_port" == "y" ] || [ "$ssh_port" == "Y" ]; then
            echo "Ouverture du port 22 - SSH"
            sudo ufw allow 22 > /dev/null 2>&1
            break
        elif [ "$ssh_port" == "n" ] || [ "$ssh_port" == "N" ]
            echo "Quel port voulez vous utilisez?"
            read ssh_custom_port
            echo "Ouverture du port $ssh_custom_port"
            sudo ufw allow $ssh_custom_port > /dev/null 2>&1
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read ssh_port
        fi
    done
}