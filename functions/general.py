#!/usr/bin/python

import os

# 

def openssh_install ():

    print("Installation de OpenSSH Server")
    os.system("sudo apt-get install openssh-server -y > /dev/null 2>&1")
    
    ssh_port=int(input("Voulez vous utiliser le port par défaut? [y/n] "))

    while True:
        if ssh_port == "y" or "Y":
            print("Ouverture du port 22")
            os.system("sudo ufw allow 22 > /dev/null 2>&1")
            break
        elif ssh_port == "n" or "N":
            ssh_custom_port = int(input("Quel port voulez vous utilisez? "))
            print(f"Ouverture du port {ssh_custom_port}")
            os.system(f"sudo ufw allow {ssh_custom_port} > /dev/null 2>&1")
        else:
            ssh_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))
