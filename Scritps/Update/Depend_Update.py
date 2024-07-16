#Creado Por NeAnTime, Modulos Para Sofware Principal
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys

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
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
def exe(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(resultado.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando el comando: {e.stderr.decode()}")
#____________________________________________________________________________________________________


def create_txt():
    ruta_txt = os.path.join("Scritps/allFiles/")
    file_path = os.path.join(ruta_txt, 'Execute.txt')
    with open(file_path, 'w') as file:
        file.write("03358440-0e66-4adb-862d-6df7f106f4c2-XGMS7e7n2sdX-NOWGuMKBIGel-yt2Xp7ov4m6e-633oMKM5Qrle-CwtWlf0ZyPXm-NIXZFgWcSh97-tYj1NwfrmmTP-GrbSRoxhq9VW-H0TBJzTQpgC7-B6WosSV0i8tC-URaKozETAZ-3vOonS2bf4MT-5uINQmRlgtgF-b9IQssMEz7jH9di2OMoD2t9uBP7LOQ-WhIC1ryNRaG4-aSRG5J71UoIZ-AicmG5kQUP6z- 5mfLX45UDqrk - Nesantime - SyS-Tool :)")
    print("\nArchivo de Registro y cache, creado ¡exitosamente!")
    print("Se Realizara Nuevamente una Comprobacion de La Instalaciones...")
    reverse(seg=2)
    clear()

#Dependencias...

def Rel_Twilio():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', 'twilio'])
        return True
    except subprocess.CalledProcessError as e:
        print(f"No se Encuentra Instalado Twilio: {e}")
        return False
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        return False

    

#Installer...

def installer_Twilio():
    try:
        print("Se Iniciara La Instalacion...")
        subprocess.run(['pip3', 'install', 'twilio'], check=True)
        clear()
        print("La Instalacion de Twilio se Completo Correctamente...")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Twilio: {e}")
        return False
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        return False

def Submain(name, play):
    print(f"{name}, no se encuentra instalada..")
    yn = input("¿Desea Instalarla Ahora? y/n: ")

    if yn == "n":
        print("Error. No se Puede Continuar Con La Ejecucion del La Herramienta!")
        print("Descarge las Dependencias Requeridas. Error 80004001")
        input("Presione Enter Para Continuar... ")
    else:
        print(f"\nIniciando Descarga De la {play}...")


def Main():
    print("Verificando la libreria Twilio\n")
    Rel_Twilio()
    reverse(seg=2)
    
    if not Rel_Twilio():
        Submain(name="La Libreria Twilio De Python", play="Libreria")
        installer_Twilio()
        if not installer_Twilio():
            print("La instalación falló. Error 710048005")
        else:
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload...")
            reverse(seg=2)
            clear()
            subprocess.run(['python', 'SyS-Tool_Install.py'])
    
    else:
        print("Todas Las Herramientas y Dependencias Se Encuentran Instaladas...")
        create_txt()
        reverse(seg=1)
        print("Iniciando el Payload...")
        clear()

Main()