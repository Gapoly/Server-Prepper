#!/usr/bin/python
import distro

def sys_detec ():
# Détection de la distrib
    host_executer=distro.id()

    if host_executer == 'ubuntu':
        #executer les versions ubuntu
        #systeme="ubuntu"
        print("Système Ubuntu détecté")
        return(host_executer)
        

    elif host_executer == 'debian':
        #systeme="debian"
        print("Système Debian détecté")
        return(host_executer)
        

    else:
        #quitter le script"
        return(f" Système {host_executer} détecté. Cette distrib n'est pas supporte sur ce script. Fin du script")
        exit