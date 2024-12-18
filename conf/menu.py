#!/usr/bin/python

import subprocess
import sys

from functions.general import web_install
from functions.general import docker_install
#from functions.general import 
#from functions.general import 
from functions.general import openssh_install


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
        elif choice == 13:
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        elif choice == 14:
            subprocess.run(['bash', '-c', 'sudo apt-get upgrade -y > /dev/null 2>&1'])
            print("Merci d'avoir utilisé Server Prepper")
            sys.exit()
        else:
            print("Valeur incorrect")
            continue
