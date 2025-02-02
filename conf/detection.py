#!/usr/bin/python3
import distro

# Detection de la distri
def sys_detec ():

    host_executer=distro.id()

    if host_executer == 'ubuntu':
       
        print("Système Ubuntu détecté")
        return(host_executer)
    elif host_executer == 'debian':
        print("Système Debian détecté")
        return(host_executer)
    else:
        print(f" Système {host_executer} détecté. Cette distrib n'est pas supportée sur ce script. Fin du script")
        exit