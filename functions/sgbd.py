#!/usr/bin/python3

# 6.  MySQL
# 7.  MariaDB
# 8.  PostgreSQL

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
        
    root_mysql=input("Voulez-vous mettre un mot de passe root pour MySQL? [y/n]")
    while True:
        if root_mysql == "y" or "Y":
            mysql_passwd=input("Quel mot de passe voulez-vous utilisez? ")
            os.system(f"""sudo mysql -u root
            UPDATE mysql.user SET password=PASSWORD('{mysql_passwd}') where User="root";
            FLUSH PRIVILEGES;
            exit;""")
            print("Mot de passe root MySQL mis à jour") 
            break
        elif root_mysql == "n" or "N":
            break
        else:
            mysql_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))

    mysql_db=input(int("Voulez-vous créer une base de données? [y/n]"))
    while True:
        if mysql_db == "y" or "Y":
            mysql_db_name=input("Quel nom voulez-vous donnez à votre base de données?")
            os.system(f"sudo mysql -u root -p {mysql_passwd} -e 'CREATE DATABASE {mysql_db_name};'")
            break
        elif mysql_db == "n" or "N":
            break
        else:
            mysql_db=input(int("Choix incorrect. Veuillez entrer 'y' ou 'n' "))

def mariadb_install ():

    print("Installation de MariaDB")
    os.system("sudo apt-get install mariadb -y > /dev/null 2>&1")

    mariadb_port=int(input("Voulez vous utiliser le port par défaut? [y/n]"))
    while True:
        if mysql_port == "y" or "Y":
            print("Ouverture du port 3306")
            os.system("sudo ufw allow 3306")
            break
        elif mariadb_port == "n" or "N":
            mariadb_port=int(input("Quel port voulez-vous utilisez?"))
            print(f"Ouverture du port {mariadb_port}")
            os.system(f"sudo ufw allow {mariadb_port}")
            break
        else:
            mariadb_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))
        
    root_mariadb=input("Voulez-vous mettre un mot de passe root pour MySQL? [y/n]")
    while True:
        if root_mariadb == "y" or "Y":
            mariadb_passwd=input("Quel mot de passe voulez-vous utilisez? ")
            os.system(f"""sudo mysql -u root
            UPDATE mysql.user SET password=PASSWORD('{mariadb_passwd}') where User="root";
            FLUSH PRIVILEGES;
            exit;""")
            print("Mot de passe root MySQL mis à jour") 
            break
        elif root_mariadb == "n" or "N":
            break
        else:
            mysql_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))

    mariadb_db=input(int("Voulez-vous créer une base de données? [y/n]"))
    while True:
        if mariadb_db == "y" or "Y":
            mariadb_db_name=input("Quel nom voulez-vous donnez à votre base de données?")
            os.system(f"sudo mysql -u root -p {mariadb_passwd} -e 'CREATE DATABASE {mariadb_db_name};'")
            break
        elif mysql_db == "n" or "N":
            break
        else:
            mysql_db=input(int("Choix incorrect. Veuillez entrer 'y' ou 'n' "))

def postgresql_install ():

    print("Installation de PostgreSQL")
    os.system("sudo apt-get install postgresql -y > /dev/null 2>&1")

    postgresql_port=int(input("Voulez vous utiliser le port par défaut? [y/n]"))
    while True:
        if postgresql_port == "y" or "Y":
            print("Ouverture du port 5432")
            os.system("sudo ufw allow 5432")
            break
        elif postgresql_port == "n" or "N":
            postgresql_port=int(input("Quel port voulez-vous utilisez?"))
            print(f"Ouverture du port {postgresql_port}")
            os.system(f"sudo ufw allow {postgresql_port}")
            break
        else:
            postgresql_port=int(input("Choix incorrect. Veuillez entrer 'y' ou 'n' "))
        
    root_postgresql=input("Voulez-vous changez le mot de passe par défaut de PostgreSQL? (password) [y/n] ")
    while True:
        if root_postgresql == "y" or "Y":
            postgresql_passwd=input("Quel mot de passe voulez-vous utilisez? ")
            os.system(f"""sudo -u postgres psql -c "ALTER USER postgres PASSWORD '{postgresql_passwd}';" """)
            print("Mot de passe root PostgreSQL mis à jour") 
            break
        elif root_postgresql == "n" or "N":
            break
        else:
            root_postgresql=input("Choix incorrect. Veuillez entrer 'y' ou 'n' ")