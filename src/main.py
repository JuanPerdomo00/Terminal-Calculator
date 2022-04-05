#!/usr/bin/python3
# Coding: utf-8

# Este software es Libre Travaja bajo la GPLv3

###################################################
# Calculadora basica extendible para terminal
# Es un proyecto simple pero de gran utilidad 
# si es que se agrega al [PATH] llamarlo como un
# comando ejecutable en (Linux)
###################################################


from colorama import Fore
import platform
import os

__Author__ = "jakepy"
__version__ = 1.0


# clase para darle color a las salidas
class Color:
    # colores
    # reset colors
    color_off: str = Fore.RESET
    g: str = Fore.GREEN
    c: str = Fore.CYAN
    r: str = Fore.RED
    m: str = Fore.MAGENTA


# Limpiamos la pantalla del prompt
def limpiar_pan():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")


# Nos pregunta si queremos continuar con el flujo del programa
def continuar():
    print(f"\n{Color.r}[!] {Color.g}Desea continuar usando el programa? {Color.color_off}")
    con: str= str(input(f"{Color.g}Si{Color.m}[s]{Color.color_off}{Color.g} o No{Color.m}[n]{Color.g}: {Color.color_off}"))
    if con == "si" or con == "s":
        limpiar_pan()
        banner()
        operations(option())
        
    elif con == "no" or con == "n":
        limpiar_pan()
        print(f"\n{Color.r}[!] {Color.g}Gracias... {Color.color_off}\n")
        exit(0)
    else:
        limpiar_pan()
        print(f"\n{Color.r}[!] {Color.g}Que haces? {Color.m}>:( {Color.color_off}\n")
        exit(2)


def option():
    print(f"""{Color.g}
        Que operaion desea hacer?
        1. Sumar 
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
          {Color.color_off}""")
    try:
        n:int =int(input(f"{Color.r}[*] {Color.g}Ingrese la opcion: {Color.color_off}"))
        return n
    except ValueError as e:
        print(f"\n{Color.r}[!] {Color.g}Que Diablos haces {Color.m}:) {Color.color_off}")
        print(e)
        exit(2)
    except KeyboardInterrupt:
        print(f"\n{Color.r}[!] {Color.g}Saliendo Forzado...{Color.color_off}")
        exit(2)

def operations(n):
    limpiar_pan()
    while n != 5:
        # sumar
        try:
            if n == 1:
                banner()
                num_a: int = int(input(f"{Color.r}[*] {Color.g}Ingrse el primer numero: {Color.color_off}"))
                num_b: int = int(input(f"{Color.r}[*] {Color.g}Ingrese el segundo numero: {Color.color_off}"))
                sum: int = num_a + num_b
                print(f"{Color.m}[+] {Color.g}La suma de {num_a} y {num_b} es: {sum} {Color.color_off}")
                continuar()

            elif n == 2:
                banner()
                num_a: int = int(input(f"{Color.r}[*] {Color.g}Ingrse el primer numero: {Color.color_off}"))
                num_b: int = int(input(f"{Color.r}[*] {Color.g}Ingrese el segundo numero: {Color.color_off}"))

                res: int = num_b - num_a
                print(f"\n{Color.m}[+] {Color.g}La resta de {num_a} y {num_b} es: {res} {Color.color_off}")
                continuar()

            elif n == 3:
                banner()
                num_a: int = int(input(f"{Color.r}[*] {Color.g}Ingrse el primer numero: {Color.color_off}"))
                num_b: int = int(input(f"{Color.r}[*] {Color.g}Ingrese el segundo numero: {Color.color_off}"))

                mul: int = num_b * num_a
                print(f"\n{Color.m}[+] {Color.g}La Mulltiplicacion de {num_a} y {num_b} es: {mul} {Color.color_off}")
                continuar()


            elif n == 4:
                banner()
                num_a: int = int(input(f"{Color.r}[*] {Color.g}Ingrse el primer numero: {Color.color_off}"))
                num_b: int = int(input(f"{Color.r}[*] {Color.g}Ingrese el segundo numero: {Color.color_off}"))

                div: float = num_a / num_b
                div: float = round(div, 2)
                print(f"\n{Color.m}[+] {Color.g}La Divicion de {num_a} y {num_b} es: {div} {Color.color_off}\n")
                continuar()
    
            elif n == 5:
                banner()
                print(f"\n{Color.r}[+] {Color.g}Bye.... {Color.color_off}\n")
                exit(1)
            
            else:
                print(f"{Color.r}[!] {Color.g}Opcion intpducida no es valida                                          {Color.m}:( {Color.color_off}")
                exit(2)
        
        except ValueError as e:
            print(f"\n{Color.r}[!]{Color.g} Ingresa numero o eres tonto?{Color.color_off}")
            print(f"{Color.g}{e}{Color.color_off}")
            exit(2)
        
        except KeyboardInterrupt:
            print(f"\n{Color.r}[!] {Color.g}Saliendo Forzado...{Color.color_off}")
            exit(2)


def banner():
    limpiar_pan()
    print(f"""{Color.g}
        =====================
        |Terminal-Calculator|
        =====================
                Author:{Color.m}{__Author__} 
          {Color.color_off}""")



def main():
    banner()
    operations(option())

if __name__=="__main__":
    main()
