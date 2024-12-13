#!/bin/bash

mysql_install () {

    echo "Installation de MySQL"
    sudo apt-get install mysql -y > /dev/null 2>&1

    echo "Voulez vous utiliser le port par défaut? [y/n]"
    read mysql_port

    while true; do
        if [ "$mysql_port" == "y" ] || [ "$mysql_port" == "Y" ]; then
            echo "Ouverture du port 3306 - MySQL"
            sudo ufw allow 3306 > /dev/null 2>&1
            break
        elif [ "$mysql_port" == "n" ] || [ "$mysql_port" == "N" ]; then
            echo "Quel port voulez vous utilisez?"
            read mysql_custom_port
            echo "Ouverture du port $mysql_custom_port"
            sudo ufw allow $mysql_custom_port > /dev/null 2>&1
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read mysql_port
        fi
    done

}

mariadb_install () {

    echo "Installation de MariaDB"
    sudo apt-get install mariadb-server -y > /dev/null 2>&1

    echo "Voulez vous utiliser le port par défaut? [y/n]"
    read mariadb_port

    while true; do
        if [ "$mariadb_port" == "y" ] || [ "$mariadb_port" == "Y" ]; then
            echo "Ouverture du port 3306 - MariaDB"
            sudo ufw allow 3306 > /dev/null 2>&1
            break
        elif [ "$mariadb_port" == "n" ] || [ "$mariadb_port" == "N" ]; then
            echo "Quel port voulez vous utilisez?"
            read mysql_custom_port
            echo "Ouverture du port $mariadb_custom_port"
            sudo ufw allow $mariadb_custom_port > /dev/null 2>&1
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read mariadb_port
        fi
    done

}

postresql_install () {


}