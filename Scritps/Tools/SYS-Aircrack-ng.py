# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time
import requests
from colorama import init, Fore, Style
init(autoreset=True)
rut = 'Scritps/allFiles/UsedRck.txt'

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        subprocess.run(["clear"])

def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    for elemento in tqdm(range(10), desc):
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

def Main():
    clear()
    Logo()
    print(Fore.BLUE + "Asistente de Auditoria WIFI\n")
    reverse(seg=3)

    if not os.path.exists(rut):
        print(f"{Fore.RED}[!] La Herramienta A Sido Iniciada Por Primera Vez, Se Descargara Los Complementos Nesesarios! .")

        file_path = os.path.join(os.path.join("Scritps/allFiles/"), 'UsedRck.txt')
        with open(file_path, 'w') as file:
            file.write("Cache execute AirCrack")

        Barra(desc="Descargando Complementos ")
        print(f"\n{Fore.GREEN}[!] Completado")
        clear()
        Main()
    
    else:
        print(Fore.CYAN + "*** Menu SYS-Crack ***")
        print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL} Descargar RockYou")
        print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL} Comandos Para Auditorias Wifi")
        print(f"{Style.BRIGHT}{Fore.BLUE}[3] {Fore.RESET}{Style.RESET_ALL} Salir")

        opc = input("\n-- Ingrese Su Opcion: ")
        if opc == "1":
            clear()
            print(Style.BRIGHT + "*** Menu Descargar RockYou ***")
            print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL} Descargar RockYou (Version Estandar)")
            print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL} Descargar RockYou (Version SyS-Tool)")
            print(f"{Style.DIM}{Fore.BLUE}[3] {Fore.RESET}{Style.RESET_ALL} Descargar RockYou (Version 2024)")
            print(f"{Style.BRIGHT}{Fore.BLUE}[3] {Fore.RESET}{Style.RESET_ALL} Salir")

            opct = input("\n--- Ingrese Su Opcion: ")
            if opct == "1":
                print(Fore.GREEN + f"[!] Descargando, ¡Tu RockYou Estara Disponible en Breves!")
                reverse(seg=2)

                resp = requests.get("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", stream=True)
                tamaño = int(resp.headers.get('content-length', 0))

                with open("RockYou.txt", "wb") as archivo:
                    with tqdm(total=tamaño, unit="B", unit_scale=True, desc="RockYou.txt", ascii=True) as barra:
                        for datos in resp.iter_content(chunk_size=1024):
                            archivo.write(datos)

                barra.update(len(datos))

                print(Fore.GREEN + "[!] DESCARGADO CON EXITO! ")
            
            elif opct == "2":
                return
            elif opct == "3":
                return
            elif opct == "4":
                print(Fore.RED + "[!] Saliendo.. ")
            else:
                print(Fore.RED + "[!] Error. El Comando No existe! ")
                Main()
        
        elif opc == "2":
            return
        
        elif opc == "3":
            print(Fore.RED + "[!] Saliendo.. ")
        else:
            print(Fore.RED + "[!] Error. El Comando No existe! ")
            Main()

Main()