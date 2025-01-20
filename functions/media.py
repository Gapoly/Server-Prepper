#!/usr/bin/python3

# 9.  Minecraft
# 10. qBittorrent

import os

def minecraft_install ():
    print("Installation des packages nécessaires")
    os.system("sudo apt-get install default-jre openjdk-17-jre-headless sed screen -y > /dev/null 2>&1")
    os.system("""sudo mkdir /minecraft-server
              wget /minecraft-server/server.jar https://piston-data.mojang.com/v1/objects/4707d00eb834b446575d89a61a11b5d548d8c001/server.jar
              echo "eula=true" > /minecraft-server/eula.txt""")
    print("Ouverture du port 25565")
    os.system("sudo ufw allow 25565")
    os.system("screen -S minecraft java -Xmx1024M -Xms1024M -jar /minecraft-server/server.jar nogui")
