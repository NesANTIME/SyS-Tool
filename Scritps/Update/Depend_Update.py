#Creado Por NeAnTime, Modulos Para Sofware Principal
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys
from colorama import init, Fore, Style
import random
import string

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(20)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
def exe(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(resultado.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando el comando: {e.stderr.decode()}")
init(autoreset=True)
#____________________________________________________________________________________________________
def create_txt():
    ruta_txt = os.path.join("Scritps/allFiles/")
    file_path = os.path.join(ruta_txt, 'Execute.txt')
    with open(file_path, 'w') as file:
        caden = ''.join(random.choices(string.ascii_letters + string.digits, k=90))
        file.write(caden + "- SySTool.Nesantime ")

#Dependencias...
def Rel_Twilio():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', 'twilio'])
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[!] No se Encuentra Instalado Twilio: {e}")
        return False
    except Exception as e:
        print(f"{Fore.RED}[!] Se ha producido un error inesperado: {e}")
        return False

#Installer...
def installer_Twilio():
    try:
        print(Fore.GREEN + Style.DIM + "[!] Se Iniciara La Instalacion...")
        subprocess.run(['pip3', 'install', 'twilio'], check=True)
        clear()
        print(Fore.GREEN + "[!] La Instalacion de Twilio se Completo Correctamente...")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[!] Error al instalar Twilio: {e}")
        return False
    except Exception as e:
        print(f"{Fore.RED}[!] Se ha producido un error inesperado: {e}")
        return False

def Submain(name, play):
    print(f"\n{Fore.YELLOW}{Style.DIM}[x] {name}, no se encuentra instalada..")
    yn = input("¿Desea Instalarla Ahora? y/n: ")
    if yn == "n":
        print(Fore.RED + "[!] Error. No se Puede Continuar Con La Ejecucion del La Herramienta!")
        print(Fore.RED + "[!] Descarge las Dependencias Requeridas. Error 80004001")
        input(Fore.YELLOW + "Presione Enter Para Continuar... ")
    else:
        print(f"\n{Fore.GREEN}{Style.DIM} [!] Iniciando Descarga De la {play}...")


def Main():
    print(Fore.GREEN + Style.BRIGHT + "[+] Verificando la libreria Twilio\n")
    Rel_Twilio()
    reverse(seg=1)
    
    if not Rel_Twilio():
        Submain(name="La Libreria Twilio De Python", play="Libreria")
        installer_Twilio()
        if not installer_Twilio():
            print(Fore.RED + "[!] La instalación falló. Error 710048005")
        else:
            Barra(desc="Verificando La Instalacion ")
            print(Fore.YELLOW + "\n[!] Se Reiniciara El Instalador...")
            reverse(seg=1)
            clear()
            Main()
    
    else:
        print(Fore.GREEN + "[!] Todas Las Herramientas y Dependencias Se Encuentran Instaladas...")
        create_txt()
        reverse(seg=1)
        print("Iniciando el Payload...")
        clear()

Main()