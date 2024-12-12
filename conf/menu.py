#!/usr/bin/python

import subprocess

def menu ():

    while True:

        print("""
1. Web
2. Docker
3. SSH
""")
        choice=int(input("Choisissez le type de serveur que vous voulez créer : "))

        if choice == 1:
            print("""
1. Apache2
2. Nginx (ne marche pas)
""")
            choice_web=int(input("Choisissez le serveur web que vous voulez créer : "))
            if choice_web == 1:
                print("Installation de Apache2")
                subprocess.run(['bash', '-c', 'source ./functions/apache2.sh && apache2'])