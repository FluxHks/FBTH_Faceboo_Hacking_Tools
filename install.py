#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Back, Fore, init
import time

print(Fore.CYAN + """
        ███████╗██████╗ ████████╗██╗  ██╗
        ██╔════╝██╔══██╗╚══██╔══╝██║  ██║
        █████╗  ██████╔╝   ██║   ███████║
        ██╔══╝  ██╔══██╗   ██║   ██╔══██║
        ██║     ██████╔╝   ██║   ██║  ██║
        ╚═╝     ╚═════╝    ╚═╝   ╚═╝  ╚═╝ v1.0
""" + Fore.RESET)

while True:
    requ = input(Fore.BLUE + "	Instalar la herramienta " + Fore.RESET + Fore.GREEN + "y" + Fore.RESET + Fore.BLUE + "/" + Fore.RESET + Fore.RED + "n" + Fore.RESET + Fore.BLUE + " ? [" + Fore.RESET + Fore.CYAN + time.strftime("%H:%M:%S") + Fore.RESET + Fore.BLUE + "] >>> " + Fore.RESET)

    if requ == "y" or requ == "Y":
        print("\	Instalando lo necesario para usarse ...")
        os.system("pwd > ruta.txt")
        ruta = open("ruta.txt", "r")
        rute = ruta.read()
        ruta.close()
        palabras = rute.splitlines()
        rutwds = (palabras[0])
        os.system("rm -r ruta.txt")
        print(" Creando directorios y clonando herramientas ... [*]")
        os.system("mkdir " + str(rutwds) + "/FbTools")
        rutpid = (rutwds + "/FbTools")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/Cyb0r9/SocialBox")
        os.system("cd " + str(rutpid) + "/SocialBox && chmod +x SocialBox.sh && chmod +x install-sb.sh && ./install-sb.sh")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/Mebus/cupp")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/xHak9x/fbi")
        os.system("apt install git python2")
        os.system("cd " + str(rutpid) + "/fbi && chmod +x requirements.txt && chmod +x fbi.py && pip2 install -r requirements.txt")
        os.system("apt-get install setoolkit")
        os.system("apt-get install php")
        os.system("apt-get install apache2")
        os.system("apt-get install perl && cd " + str(rutpid) + " && git clone https://github.com/1uh/Zhacker.pl && cd Zhacker.pl && chmod +x Zhacker.pl")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/thelinuxchoice/shellphish")
        os.system("cd " + str(rutpid) + "/shellphish && chmod +x shellphish.sh")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/thelinuxchoice/blackeye")
        os.system("cd " + str(rutpid) + "/blackeye && chmod +x blackeye.sh")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/thelinuxchoice/saycheese")
        os.system("cd " + str(rutpid) + "/saycheese && chmod +x saycheese.sh && chmod +x saycheese.html && chmod +x post.php && chmod +x ip.php && chmod +x template.php")
        os.system("cd " + str(rutpid) + " && git clone https://github.com/BullsEye0/google_dork_list.git")
        os.system("cd " + str(rutpid) + "/google_dork_list && chmod +x google_Dorks.txt")
        break
    elif requ == "n" or "N":
        break
    else:
        continue
# comprobacion de modulos instalados ...
os.system("pwd > rutz.txt")
rutz = open("rutz.txt", "r")
leters = rutz.read()
murelist = leters.splitlines()
valor = (murelist[0])
os.system("rm -r " + str(valor) + "/rutz.txt")
rutpid = (str(valor) + "/FbTools")
os.system("ls " + str(rutpid) + " > " + str(rutpid) + "/listener.txt")
archb = open(str(rutpid) + "/listener.txt", "r")
lista = archb.read()
morelist = lista.splitlines()
cantidad1 = (morelist[8])
cantidad2 = (morelist[7])
cantidad3 = (morelist[6])
cantidad4 = (morelist[5])
cantidad5 = (morelist[4])
cantidad6 = (morelist[3])
cantidad7 = (morelist[2])
cantidad8 = (morelist[1])
cantidad9 = (morelist[0])
archb.close()
if cantidad1 == "Zhacker.pl" and cantidad2 == "SocialBox" and cantidad3 == "shellphish" and cantidad4 == "saycheese" and cantidad5 == "listener.txt" and cantidad6 == "google_dork_list" and cantidad7 == "fbi" and cantidad8 == "cupp" and cantidad9 == "blackeye":
    print(Fore.RED + "\n        Advertencia " + Fore.RESET + Fore.CYAN + ": No agrege directorios o modifique\n        el nombre Dentro de la carpeta " + Fore.RESET + Fore.GREEN + "[ FbTools/ ]" + Fore.RESET + Fore.CYAN + " ya\n        que puede causar problemas al correr esta herramienta ... " + Fore.RESET)
    print(Fore.GREEN + "        Modulos correctamente instalados ... [" + Fore.RESET + Fore.YELLOW + "*" + Fore.RESET + Fore.GREEN + "]\n" + Fore.RESET)
else:
    print(Fore.RED + "\n        Advertencia " + Fore.RESET + Fore.CYAN + ": No agrege directorios o modifique\n        el nombre Dentro de la carpeta " + Fore.RESET + Fore.GREEN + "[ FbTools/ ]" + Fore.RESET + Fore.CYAN + " ya\n        que puede causar problemas al correr esta herramienta ... " + Fore.RESET)
    print(Fore.RED +"        Error al cargar los modulos, Ejecute\n        denuevo el programa o tome encuenta el mensaje de arriba" + Fore.RESET)
    exit()
