#!/bin/bash



echo "Lancement des mises à jours"

sudo apt-get update > /dev/null 2>&1

echo "Installation des mises à jours"

sudo apt-get upgrade -y && sudo apt-get install ufw -y > /dev/null 2>&1