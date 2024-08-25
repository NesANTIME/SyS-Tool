import os
import urllib.request
from colorama import init, Fore, Style
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------------
def Not_Version():
    if os.path.isfile(os.path.join("Scritps/allFiles/", 'NewUpdate.txt')):
        try:
            os.remove(os.path.join("Scritps/allFiles/", 'NewUpdate.txt'))
        except Exception as e:
            print(f"{Fore.RED}[!] Error al eliminar El Archivo de Version: {e}")

def New_Version(V_NewUp):
    with open(os.path.join("Scritps/allFiles/", 'NewUpdate.txt'), 'w') as file:
        file.write(f"[!] La Nueva Version de {V_NewUp} Esta disponible ¡Descargala YA!\n")

def Update():
    VerLocal = 'Scritps/allFiles/Install.txt'
    VerNew = "https://raw.githubusercontent.com/NesANTIME/SyS-Tool/main/Version.txt"
    
    def V_NewVer(VerNew):
        try:
            with urllib.request.urlopen(VerNew) as response:
                contenido = response.read().decode('utf-8').strip()
                return contenido
        except Exception as e:
            print(f"{Fore.RED}[!] No se pudo obtener el contenido remoto: {e}")
            return None
        
    def V_LocalVer(VerLocal, V_Newup):
        try:
            if not os.path.exists(VerLocal):
                print(f"{Fore.RED}[!] El archivo local {VerLocal} no existe.")
                return
            
            with open(VerLocal, 'r') as file:
                contenido_local = file.read().strip()
                if contenido_local == V_NewUp:
                    Not_Version()
                else:
                    New_Version(V_NewUp)
        except Exception as e:
            print(f"{Fore.RED}[!] Error al leer el archivo local {VerLocal}: {e}")

    V_NewUp = V_NewVer(VerNew)
    if V_NewUp is not None:
        V_LocalVer(VerLocal, V_NewUp)
    else:
        print(Fore.RED + "[!] No se pudo obtener el contenido remoto para comparar.")

Update()