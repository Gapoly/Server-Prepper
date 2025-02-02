#!/usr/bin/python3

import sys

from functions.general import *
from functions.sgbd import *
from functions.media import *
from functions.vpn import *

def menu ():

    while True:

        print("""
1.  Web
2.  Docker
3.  SSH
              
SGBD :
4.  MySQL
5.  MariaDB
6.  PostgreSQL
              
Multimédia :
7.  Minecraft
8. qBittorrent
              
VPN :
9. Wireguard
10. OpenVPN          
              
11. Exit
12. Upgrade & Exit
""")
        choice=int(input("Choisissez le type de serveur que vous voulez créer : "))

        if choice == 1:
            web_install()
        elif choice == 2:
            docker_install()
        elif choice == 3:
            openssh_install()

        elif choice == 4:
            mysql_install()
        elif choice == 5:
            mariadb_install()
        elif choice == 6:
            postgresql_install()

        elif choice == 7:
            minecraft_install()
        elif choice == 8:
            qbittorrent_install()

        elif choice == 9:
            wireguard_install()
        elif choice == 10:
            openvpn_install()
        
        elif choice == 11:
            print("Activation du Pare-feu")
            os.system("sudo ufw enable")
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        elif choice == 12:
            print("Installation des mises à jours")
            os.system("sudo apt-get upgrade -y > /dev/null 2>&1")
            print("Activation du Pare-feu")
            os.system("sudo ufw enable")
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        else:
            print("Valeur incorrect")
            continue
