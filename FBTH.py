#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Back, Fore, init
import time

os.system("pwd > rutz.txt")
rutz = open("rutz.txt", "r")
leters = rutz.read()
murelist = leters.splitlines()
valor = (murelist[0])
os.system("rm -r " + str(valor) + "/rutz.txt")
rutpid = (str(valor) + "/FbTools")
print(Fore.CYAN + """
        ███████╗██████╗ ████████╗██╗  ██╗
        ██╔════╝██╔══██╗╚══██╔══╝██║  ██║
        █████╗  ██████╔╝   ██║   ███████║
        ██╔══╝  ██╔══██╗   ██║   ██╔══██║
        ██║     ██████╔╝   ██║   ██║  ██║
        ╚═╝     ╚═════╝    ╚═╝   ╚═╝  ╚═╝ v0.1
""" + Fore.RESET)
#comprobacion de modulos

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

print(Fore.GREEN + """
   +-------------------------------------------------------------+
   | Opciones:                                                   |
   +-------------------------------------------------------------+
   |[1] Zhacker.pl      [4] saycheese       [7] blackeye         |
   |[2] SocialBox       [5] FBI             [8] Google Dork List |
   |[3] shellphish      [6] cupp                                 |
   +-------------------------------------------------------------+
 """ + Fore.RESET)
while True:
    banner = (Fore.CYAN + """
            ███████╗██████╗ ████████╗██╗  ██╗
            ██╔════╝██╔══██╗╚══██╔══╝██║  ██║
            █████╗  ██████╔╝   ██║   ███████║
            ██╔══╝  ██╔══██╗   ██║   ██╔══██║
            ██║     ██████╔╝   ██║   ██║  ██║
            ╚═╝     ╚═════╝    ╚═╝   ╚═╝  ╚═╝ v0.1
    """ + Fore.RESET + Fore.GREEN + """
   +-------------------------------------------------------------+
   | Opciones:                                                   |
   +-------------------------------------------------------------+
   |[1] Zhacker.pl      [4] saycheese       [7] blackeye         |
   |[2] SocialBox       [5] FBI             [8] Google Dork List |
   |[3] shellphish      [6] cupp                                 |
   +-------------------------------------------------------------+
     """ + Fore.RESET)
    selectol = input(Fore.BLUE + "       Select [" + Fore.RESET + Fore.CYAN + time.strftime("%H:%M:%S") + Fore.RESET + Fore.BLUE + "]-->>> " + Fore.RESET)
    if selectol == "1":
         print(Fore.WHITE + "                               Version 2.32" + Fore.RESET)
         print(Fore.GREEN + """d88888b  .d8b.   .o88b. d88888b d8888b.  .d88b.  db   dD d88888b d8888b.
88'     d8' `8b d8P  Y8 88'     88  `8D .8P  Y8. 88 ,8P' 88'     88  `8D
88ooo   88ooo88 8P      88ooooo 88oooY' 88    88 88,8P   88ooooo 88oobY'
88~~~   88~~~88 8b      88~~~~~ 88~~~b. 88    88 88`8b   88~~~~~ 88`8b
88      88   88 Y8b  d8 88.     88   8D `8b  d8' 88 `88. 88.     88 `88.
YP      YP   YP  `Y88P' Y88888P Y8888P'  `Y88P'  YP   YD Y88888P 88   YD """ + Fore.RESET)
         print(Fore.RED + "          ======================================================" + Fore.RESET)
         email = input("\n        E-mail >>> ")
         print(Fore.BLUE + "        Email [ " + Fore.RESET + Fore.GREEN + str(email) + Fore.RESET + Fore.BLUE + " ] Añadido." + Fore.RESET)
         dict = input("        Diccionario >>> ")
         print(Fore.BLUE + "        Diccionario [ " + Fore.RESET + Fore.GREEN + str(dict) + Fore.RESET + Fore.BLUE + " ] Añadido" + Fore.RESET)
         print(Fore.RED + "\n          ======================================================" + Fore.RESET)
         os.system("cd " + str(rutpid) + "/Zhacker.pl/ && perl Zhacker.pl " + str (email) + " " + str(dict))
    elif selectol == "2":
         os.system("cd " + str(rutpid) + "/SocialBox && bash SocialBox.sh")
    elif selectol == "3":
         os.system("cd " + str(rutpid) + "/shellphish && bash shellphish.sh")
    elif selectol == "4":
         os.system("cd " + str(rutpid) + "/saycheese && bash saycheese.sh")
    elif selectol == "5":
         os.system("cd " + str(rutpid) + "/fbi && python fbi.py")
    elif selectol == "6":
         os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py > helper.txt && chmod +x helper.txt && cat helper.txt")
         print("  -b, --banner       Banner for Cupp tool (print banner)")
         print("  -e, --exit         Exit from interactive prompt (exit tool)")
         print("  -c, --clear        Cleaning terminal (cleaner terminal)\n")
         while True:
             pront = input(Fore.BLUE + "       Interactive Prompt >>> " + Fore.RESET)
             if pront == "-i" or pront == "--interactive":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -i")
             elif pront == "--help" or pront == "-h":
                 print(" ")
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -h")
                 print("  -b, --banner       Banner for Cupp tool (print banner)")
                 print("  -e, --exit         Exit from interactive prompt (exit tool)")
                 print("  -c, --clear        Cleaning terminal (cleaner terminal)\n")
             elif pront == "-v" or pront == "--version":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -v")
             elif pront == "-l":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -l")
             elif pront == "-w":
                 dirchar = input(Fore.GREEN + "       Ruta del archivo >>> " + Fore.RESET)
                 print(Fore.GREEN + "       Ruta [ " + Fore.RESET + Fore.YELLOW + str(dirchar) + Fore.RESET + Fore.GREEN + " ] añadida ... Ok" + Fore.RESET)
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -w " + str(dirchar))
             elif pront == "-q" or pront == "--quiet":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -q")
             elif pront == "-a":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py -a")
             elif pront == "-e" or pront == "--exit":
                 break
             elif pront == "-b" or pront == "--banner":
                 os.system("cd " + str(rutpid) + "/cupp && python3 cupp.py > helper.txt && chmod +x helper.txt && cat helper.txt")
                 print("  -b, --banner       Banner for Cupp tool (print banner)")
                 print("  -e, --exit         Exit from interactive prompt (exit tool)")
                 print("  -c, --clear        Cleaning terminal (cleaner terminal)\n")
             elif pront == "-c" or pront == "--clear":
                 os.system("clear")
             else:
                 pass
    elif selectol == "7":
         os.system("cd " + str(rutpid) + "/blackeye && bash blackeye.sh")
    elif selectol == "8":
         os.system("cd " + str(rutpid) + "/google_dork_list && nano google_Dorks.txt")
    elif selectol == "banner":
         print(banner)
    elif selectol == "help" or selectol == "-h":
         print (Fore.GREEN + "       [+] " + Fore.RESET + Fore.YELLOW + "COMANDS FBTH" + Fore.RESET + Fore.GREEN + " [+]")
         print (Fore.GREEN + """
       [*] exit o quit { Salir de FBTH }
       [*] clear o cls { Limpiar pantalla }
       [*] banner      { Banner de Tools List }
       [*] ifconfig    { Comando para mostrar ip }
          """)
         print (Fore.GREEN + "       [+] " + Fore.RESET + Fore.YELLOW + "TOOLS LIST" + Fore.RESET + Fore.GREEN + " [+]")
         print (Fore.GREEN + """
       [1] Zhacker.pl { Ataque de fuerza bruta }
       [2] SocialBox  { Toolkit de Fuerza Bruta hacia redes sociales ... }
       [3] shellphish { Phishing a Instagram, Facebook, Snapchat, etc ... }
       [4] saycheese  { Espia webcams desde un link ;-) }
       [5] FBI        { Facebook Gathering Information, Recolector de
                        informacion de una cuenta de Facebook comprometida }
       [6] cupp       { Creador de diccionarios de Fuerza bruta + Prompt Interactivo }
       [7] blackeye   { Phishing a Redes sociales dentro de LAN }
       [8] Google_Dorks { Bonus de Hacking ;-) }
          """ + Fore.RESET)
         print (Fore.WHITE + "       [+]" + Fore.RESET + Fore.RED + "                      Coded By FluxHack         		   " + Fore.RESET + Fore.WHITE + "[+]" + Fore.RESET)
         print (Fore.WHITE + "       [+]" + Fore.RESET + Fore.RED + "        https://www.facebook.com/groups/667611437051055 	   " + Fore.RESET + Fore.WHITE + "[+]" + Fore.RESET)
         print (Fore.WHITE + "       [+]" + Fore.RESET + Fore.RED + "             https://k3y4cc3ss-42.000webhostapp.com          " + Fore.RESET + Fore.WHITE + "    [+]" + Fore.RESET)
         print (Fore.WHITE + "       [+]" + Fore.RESET + Fore.RED + " 	       Agradecimientos especiales a : { " + Fore.RESET + Fore.GREEN + "GoldenL" + Fore.RESET + Fore.RED + " }          " + Fore.RESET + Fore.WHITE + "[+]\n" + Fore.RESET)
    elif selectol == "exit" or selectol == "quit":
        print (Fore.RED + "       Saliendo ... " + Fore.RESET + Fore.GREEN + "[Ok] \n" + Fore.RESET)
        break
        exit()
    elif selectol == "clear" or selectol == "cls":
        os.system("clear")
    elif selectol == "ifconfig":
        print(" ")
        os.system("ifconfig")
    else:
        continue
