#!/usr/bin/python3

import os

def mysql_install ():

    print("Installation de MySQL")
    os.system("sudo apt-get install mysql -y > /dev/null 2>&1")

    mysql_port=int(input("Voulez vous utiliser le port par défaut? [y/n]"))

    while True:
        if mysql_port == "y" or "Y":
            print("Ouverture du port 3306")
            os.system("sudo ufw allow 3306")
            break
        elif mysql_port == "n" or "N":
            mysql_port=int(input("Quel port voulez-vous utilisez?"))
            print(f"Ouverture du port {mysql_port}")
            os.system(f"sudo ufw allow {mysql_port}")
            break
        else:
            mysql_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))