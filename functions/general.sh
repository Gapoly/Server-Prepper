#!/bin/bash

# 1. Docker
# 2. OpenSSH Server
# 3. Web


docker_install () {

  host_executer=$(python3 ./conf/detection.py)

  if [[ "$host_executer" == "ubuntu" ]]; then
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

  else [[ "$host_executer" == "debian" ]]; then
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi
}

openssh_install () {

    echo "Installation de OpenSSH Server"
    sudo apt-get install openssh-server -y > /dev/null 2>&1

    echo "Voulez vous utiliser le port par défaut? [y/n]"
    read ssh_port

    while true; do
        if [ "$ssh_port" == "y" ] || [ "$ssh_port" == "Y" ]; then
            echo "Ouverture du port 22 - SSH"
            sudo ufw allow 22 > /dev/null 2>&1
            break
        elif [ "$ssh_port" == "n" ] || [ "$ssh_port" == "N" ]; then
            echo "Quel port voulez vous utilisez?"
            read ssh_custom_port
            echo "Ouverture du port $ssh_custom_port"
            sudo ufw allow $ssh_custom_port > /dev/null 2>&1
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read ssh_port
        fi
    done
}

web_install() {
    echo "Installation d'Apache2"
    sudo apt-get install apache2 -y > /dev/null 2>&1

    echo "Voulez-vous installer PHP et ses dépendances ? [y/n]"
    read php_choice

    while true; do
        if [ "$php_choice" == "y" ] || [ "$php_choice" == "Y" ]; then
            echo "Installation de PHP et de ses dépendances..."
            sudo apt-get install php curl php-curl -y > /dev/null 2>&1
            break
        elif [ "$php_choice" == "n" ] || [ "$php_choice" == "N" ]; then
            echo "Installation de PHP annulée."
            break
        else
            echo "Choix incorrect. Veuillez entrer 'y' ou 'n'."
            read php_choice
        fi
    done

    while true; do
        echo ""

        cat << EOF
Quel port voulez vous ouvrir?

1. 80 - HTTP
2. 443 - HTTPS
3. 80 & 443
4. Autre
EOF
        read web_port
        if [ "$web_port" == "1" ]; then
            echo "Ouverture du port 80"
            sudo ufw allow 80
            break
        elif [ "$web_port"  == "2" ]; then
            echo "Ouverture du port 443"
            sudo ufw allow 443
            break
        elif [ "$web_port"  == "3" ]; then
            echo "Ouverture du port 80 & 443"
            sudo ufw allow 80
            sudo ufw allow 443
            break
        elif [ "$web_port"  == "4" ]; then
            echo "Choisissez votre port"
            read custom_port
            sudo ufw allow $custom_port
            break
        else
            echo "Valeur incorrect"
            continue
        fi
    done
}