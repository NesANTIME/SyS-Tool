import os
import urllib.request
from colorama import init, Fore, Style
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------------
def Not_Version():
    pathy = os.path.join("Scritps/allFiles/", 'NewUpdate.txt')
    if os.path.isfile(pathy):
        try:
            os.remove(pathy)
        except Exception as e:
            print(f"{Fore.RED}[!] Error al eliminar {pathy}: {e}")

def New_Version(contenido_remoto):
    pathyt = os.path.join("Scritps/allFiles/", 'NewUpdate.txt')
    with open(pathyt, 'w') as file:
        file.write(f"[!] La Nueva Version de {contenido_remoto} Esta disponible ¡Descargala YA!\n")

def Update():
    VerLocal = 'Scritps/allFiles/Install.txt'
    VerNew = "https://raw.githubusercontent.com/NesANTIME/SyS-Tool/main/Version.txt"
    
    def Verificar_New_Ver(VerNew):
        try:
            with urllib.request.urlopen(VerNew) as response:
                contenido = response.read().decode('utf-8').strip()
                return contenido
        except Exception as e:
            print(f"{Fore.RED}[!] No se pudo obtener el contenido remoto: {e}")
            return None
        
    def Local(VerLocal, contenido_remoto):
        try:
            if not os.path.exists(VerLocal):
                print(f"{Fore.RED}[!] El archivo local {VerLocal} no existe.")
                return
            
            with open(VerLocal, 'r') as file:
                contenido_local = file.read().strip()
                if contenido_local == contenido_remoto:
                    Not_Version()
                else:
                    New_Version(contenido_remoto)
        except Exception as e:
            print(f"{Fore.RED}[!] Error al leer el archivo local {VerLocal}: {e}")

    contenido_remoto = Verificar_New_Ver(VerNew)
    if contenido_remoto is not None:
        Local(VerLocal, contenido_remoto)
    else:
        print(Fore.RED + "[!] No se pudo obtener el contenido remoto para comparar.")

Update()