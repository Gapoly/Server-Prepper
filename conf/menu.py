#!/usr/bin/python

import subprocess

def menu ():

    while True:

        print("""
1. Web
2. Docker
3. Uptime Kuma
4. Code Server
5. SSH
              
SGBD :
6. MySQL
7. MariaDB
8. PostgreSQL

              
Multimédia :
9. Minecraft
10. qBittorrent
              
VPN :
11. Wireguard
12. OpenVPN          
              
13. Exit
""")
        choice=int(input("Choisissez le type de serveur que vous voulez créer : "))

        if choice == 1:
            subprocess.run(['bash', '-c', 'source ./functions/web.sh && web_install'])
        elif choice == 2:
            subprocess.run(['bash', '-c', 'source ./functions/docker.sh && docker_install'])
        elif choice == 5:
            subprocess.run(['bash', '-c', 'source ./functions/openssh.sh && openssh_install'])
        elif choice == 13:
            exit
        else:
            print("Valeur incorrect")
            continue