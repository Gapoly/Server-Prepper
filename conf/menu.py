#!/usr/bin/python

import subprocess

def menu ():

    while True:

        print("""
1. Web
2. Docker
3. SSH
              
4. Exit
""")
        choice=int(input("Choisissez le type de serveur que vous voulez créer : "))

        if choice == 1:
            subprocess.run(['bash', '-c', 'source ./functions/web.sh && web_install'])
        elif choice == 2:
            subprocess.run(['bash', '-c', 'source ./functions/docker.sh && docker_install'])
        elif choice == 3:
            subprocess.run(['bash', '-c', 'source ./functions/openssh.sh && openssh_install'])
        elif choice == 4:
            exit
        else:
            print("Valeur incorrect")
            continue