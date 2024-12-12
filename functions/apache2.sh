#!/bin/bash


echo "Installation d'Apache2"


sudo apt-get install apache2 -y



echo "Voulez vous installer PHP et ses dépendances? [y/n]"
read php_choice


while true; do
    if ["$php_coice" == y]; then
        sudo apt-get install php curl php-curl -y
    elif ["$php_coice" == n]; then
        break
    else

    fi
done
