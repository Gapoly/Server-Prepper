#!/usr/bin/python

import subprocess
import sys

from functions.general import *
from functions.sgbd import *
from functions.media import *

def menu ():

    while True:

        print("""
1.  Web
2.  Docker
3.  Uptime Kuma
4.  Code Server
5.  SSH
              
SGBD :
6.  MySQL
7.  MariaDB
8.  PostgreSQL
              
Multimédia :
9.  Minecraft
10. qBittorrent
              
VPN :
11. Wireguard
12. OpenVPN          
              
13. Exit
14. Upgrade & Exit
""")
        choice=int(input("Choisissez le type de serveur que vous voulez créer : "))

        if choice == 1:
            web_install()
        elif choice == 2:
            docker_install()
        elif choice == 5:
            openssh_install()
        elif choice == 6:
            mysql_install()
        elif choice == 7:
            mariadb_install()
        elif choice == 8:
            postgresql_install()
        elif choice == 9:
            minecraft_install()
        elif choice == 13:
            print("Activation du Pare-feu")
            os.system("sudo ufw enable")
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        elif choice == 14:
            print("Installation des mises à jours")
            os.system("sudo apt-get upgrade -y > /dev/null 2>&1")
            print("Activation du Pare-feu")
            os.system("sudo ufw enable")
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        else:
            print("Valeur incorrect")
            continue
