#!/usr/bin/python
import distro

def sys_detec ():
# Détection de la distrib
    host_executer=distro.id()

    if host_executer == 'ubuntu':
        #executer les versions ubuntu
        return("Système Ubuntu détecté")
        systeme="ubuntu"

    elif host_executer == 'debian':
        # executer les versions Debian
        return("Système Debian détecté")
        systeme="debian"

    else:
        #quitter le script"
        return(f" Système {host_executer} détecté. Cette distrib n'est pas supporte sur ce script. Fin du script")
        exit