#!/usr/bin/python3

# 7.  Minecraft
# 8. qBittorrent

import os

def minecraft_install ():
    print("Installation des packages nécessaires")
    os.system("sudo apt-get install default-jre openjdk-17-jre-headless screen -y > /dev/null 2>&1")
    os.system("""sudo mkdir /minecraft-server
              sudo wget /minecraft-server/server.jar https://piston-data.mojang.com/v1/objects/4707d00eb834b446575d89a61a11b5d548d8c001/server.jar
              sudo echo "eula=true" > /minecraft-server/eula.txt""")
    print("Ouverture du port 25565")
    os.system("sudo ufw allow 25565")
    os.system("screen -S minecraft java -Xmx2048M -Xms1024M -jar /minecraft-server/server.jar nogui")

def qbittorrent_install ():
    print("Installation des packages nécessaires")
    os.system("sudo apt-get install qbittorrent-nox -y > /dev/null 2>&1")
    print("Ouverture du port 8080")
    os.system("sudo ufw allow 8080")
    print("Démarrage du service")
    os.system("qbittorrent-nox")