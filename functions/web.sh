#!/bin/bash


web_install () {


    
    echo "Installation d'Apache2"
    sudo apt-get install apache2 -y > /dev/null 2>&1

    echo "Voulez vous installer PHP et ses dépendances? [y/n]"
    read php_choice


    while true; do
        if ["$php_coice" == y]; then
            sudo apt-get install php curl php-curl -y > /dev/null 2>&1
        elif ["$php_coice" == n]; then
            break
        else; then
            echo "Choix incorrect"
        fi
    done
}