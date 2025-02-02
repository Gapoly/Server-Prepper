#!/usr/bin/python3

import os

# 9. Wireguard
# 10. OpenVPN

def wireguard_install ():
    print("Installation de Wireguard")
    os.system("sudo apt-get install wireguard -y > /dev/null 2>&1")
    os.system("sudo apt-get install wireguard-tools -y > /dev/null 2>&1")
    os.system("sudo apt-get install wireguard-dkms -y > /dev/null 2>&1")
    
    print("Activation de Wireguard")
    os.system("sudo modprobe wireguard")
    os.system("sudo modprobe wireguard")

    while True:
        wg_port=int(input("Voulez-vous utilisez le port par défaut? [y/n]"))
        if wg_port == "y" or "Y":
            print("Ouverture du port 51820")
            os.system("sudo ufw allow 51820")
            break
        elif wg_port == "n" or "N":
            wg_port=int(input("Quel port voulez-vous utilisez?"))
        print(f"Ouverture du port {wg_port}")
        os.system(f"sudo ufw allow {wg_port}")
        break

    print("Activation de l'IP Forwarding")
    os.system("sudo sysctl -w net.ipv4.ip_forward=1")
    
def openvpn_install ():
    print("Installation de OpenVPN")
    os.system("sudo apt-get install openvpn -y > /dev/null 2>&1")
    os.system("sudo apt-get install easy-rsa -y > /dev/null 2>&1")
    os.system("sudo apt-get install openvpn-systemd-resolved -y > /dev/null 2>&1")
    os.system("sudo apt-get install openvpn-blacklist -y > /dev/null 2>&1")

    print("Activation de OpenVPN")
    os.system("sudo systemctl enable openvpn-server@server")
    os.system("sudo systemctl start openvpn-server@server")

    while True:
        ovpn_port=int(input("Voulez-vous utilisez le port par défaut? [y/n]"))
        if ovpn_port == "y" or "Y":
            print("Ouverture du port 1194")
            os.system("sudo ufw allow 1194")
            break
        elif ovpn_port == "n" or "N":
            ovpn_port=int(input("Quel port voulez-vous utilisez?"))
        print(f"Ouverture du port {ovpn_port}")
        os.system(f"sudo ufw allow {ovpn_port}")
        break

    print("Activation de l'IP Forwarding")
    os.system("sudo sysctl -w net.ipv4.ip_forward=1")