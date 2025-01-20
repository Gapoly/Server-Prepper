#!/usr/bin/python

import os
import sys

# 1. Web
# 2. Docker
# 3. Uptime Kuma
# 4. Code Server
# 5. SSH

def web_install ():
    print ("Installation d'Apache 2")
    os.system("sudo apt-get install apache2 -y > /dev/null 2>&1")

    php_choice=input("Voulez-vous installer PHP et ses dépendances ? [y/n] : ")

    while True:
        if php_choice == "y" or "Y":
            print("Installation de PHP et de ses dépendances")
            os.system("sudo apt-get install php curl php-curl -y > /dev/null 2>&1")
            break
        elif php_choice == "n" or "N":
            print("Installation de PHP annulée")
            break
        else:
            php_choice=input("Choix incorrect. Veuillez entrer 'y' ou 'n' ")

    while True:
        web_port=int(input("""Quel port voulez-vous ouvrir?
        
1. 80 - HTTP
2. 443 - HTTPS
3. 80 & 443
4. Autre  
        """))

        if web_port == 1:
            print("Ouverture du port 80")
            os.system("sudo ufw allow 80 > /dev/null 2>&1")
            break
        elif web_port == 2:
            print("Ouverture du port 443")
            os.system("sudo ufw allow 443 > /dev/null 2>&1")
            break
        elif web_port == 3:
            web_custom_port=int(input("Choisissez votre port : "))
            print(f"Ouverture du port {web_custom_port}")
            os.system(f"sudo ufw allow {web_custom_port}")
            break
        else:
            print("Valeur incorrect")
            continue

def docker_install ():

    from install import host

    if host == "ubuntu":
        os.system("""
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
                  
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin""")
    elif host == "debian":
        os.system("""
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin""")
    else:
        print("This was not supposed to happen")
        sys.exit()

def openssh_install ():

    print("Installation de OpenSSH Server")
    os.system("sudo apt-get install openssh-server -y > /dev/null 2>&1")
    
    ssh_port=input("Voulez vous utiliser le port par défaut? [y/n] ")

    while True:
        if ssh_port == "y" or "Y":
            print("Ouverture du port 22")
            os.system("sudo ufw allow 22 > /dev/null 2>&1")
            break
        elif ssh_port == "n" or "N":
            ssh_custom_port = int(input("Quel port voulez vous utilisez? "))
            print(f"Ouverture du port {ssh_custom_port}")
            os.system(f"sudo ufw allow {ssh_custom_port} > /dev/null 2>&1")
            break
        else:
            ssh_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))
