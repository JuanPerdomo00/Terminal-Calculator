#!/usr/bin/python3

import os
import platform

if platform.system() == "Linux":
    os.system("clear")
else:
    os.system("cls")

print("-"*90)
print("\t\t\t[*] Instalador de dependencias by: Jakepy [*]")
print("-"*90)
print("\t\t\t\t[*] Estamos Hacks :) [*]")


try:
    import colorama
    exit()

except:
    print("\n\n[!] Instalando Modulo colorama!!!\n")
    os.system("pip3 install colorama")
    print("\n[+] Moodulo de colorama Instalado...\n")
