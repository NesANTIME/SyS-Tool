import os
import time
import platform
import subprocess
from tqdm import tqdm
import urllib.request
import shutil

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
#-------------------------------------------------------------------------------------------------------------
def actualizar_registro():
    print("Felicidades, Tiene La Version Mas Reciente Del la Herramienta SyS-Tool :)")
    reverse(seg=2)
        
def obtener_directorio():
    print("Hay Una Nueva Actualizacion Disponible, ¡Descargala Ya!\n")
    print("Actualmente no se Puede Actualizar Automaticamente, Tendra que hacerlo Manualmente")
    print("Recuerde El comando Para descargarlo: (git clone https://github.com/NesANTIME/SyS-Tool.git)")
    input("\nPresione Enter Para Continuar...")

def Update():
    VerLocal = 'Scritps/allFiles/Install.txt'
    VerNew = "https://raw.githubusercontent.com/NesANTIME/SyS-Tool/main/Scritps/allFiles/Install.txt"
    
    def Verificar_New_Ver(VerNew):
        try:
            print(f"Verificando si Existe una Nueva Version: {VerNew}")
            with urllib.request.urlopen(VerNew) as response:
                contenido = response.read().decode('utf-8')
                return contenido
        except Exception as e:
            print(f"Error al Verificar: {VerNew}: {e}")
            return None
        
    def Local(VerLocal, contenido_remoto, VerNew):
        try:
            if not os.path.exists(VerLocal):
                print(f"No se encontró el archivo con la Version local: {VerLocal}")
                return
            
            print(f"Comparando Versiones:\nLocal: {VerLocal}\nRemoto: {VerNew}")
            with open(VerLocal, 'r') as file:
                contenido_local = file.read()
                if contenido_local == contenido_remoto:
                    clear()
                    actualizar_registro()
                else:
                    clear()
                    obtener_directorio()
        except Exception as e:
            print(f"Error al comparar Las Versiones: {e}")
            

    contenido_remoto = Verificar_New_Ver(VerNew)
    if contenido_remoto is not None:
        Local(VerLocal, contenido_remoto, VerNew)
    else:
        print("No se pudo obtener el contenido remoto para comparar.")

Update()
