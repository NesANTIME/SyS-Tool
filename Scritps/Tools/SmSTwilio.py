#Programa Creado Por NesAnTime
from colorama import init, Fore, Style
from twilio.rest import Client
from tqdm import tqdm
import os
import subprocess
import platform
import time
import json

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
#------------------------------------------------------------------------------------------------------

def Sub_Twilio(side, Token, NumATA, Num, mesg):
    client = Client(side, Token)

    message = client.messages.create(
        body=mesg,
        from_=NumATA,
        to=Num
        )
    print(f"El Fue Mensaje enviado Exitoxamente! to: {message.sid}")
    reverse(seg=3)
    Main()

#______________________________________________________________________________________________________

Cuentass={}

def Info_Cuentas(selec):
    carpeta = 'Scritps/cache/Acconts-SMS/'
    archivo = selec
    ruta = os.path.join(carpeta, archivo)
    
    try:
        with open(ruta, 'r') as file:
            data = json.load(file)
            print("Datos Extraidos Exitosamente!")
        return data
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta}")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {ruta}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")
        return None

def eliminar_archivo_json(selec):
    try:
        os.remove(selec)
        print(f"La Cuenta '{selec}'  se a eliminado correctamente.")
        Barra(desc="Borrando Cuenta.. ")
        reverse(seg=2)
        subprocess.run(['python', 'Scritps/Tools/SmSTWilio.py'])
        
    except FileNotFoundError:
        print(f"El archivo '{selec}' ya no existe.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar '{selec}': {e}")

def Todas_Cuentas(directorio):
    archivos_json = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.json'):
            archivos_json.append(archivo)
    return archivos_json

def Main():
    clear()
    if data:
        print("-- Informacion de Tu Cuenta...\n")
        print(f"Nombre: {data['nombre']}")
        print(f"SID: {data['SID']}")
        print(f"Token: {data['Token']}")
        print(f"Numero Local: {data['Numero Local']}\n")
        
        print("-------------------------------------------\n")
        print("¿___ Que Operacion Desea Hacer? ___")
        print("1. Enviar SMS")
        print("2. Eliminar Cuenta")
        print("3. Salir")
        op = int(input("\nIngrese Su Opcion: "))
        
        while (op < 1) or (op > 3):
            print("\nError. La Opcion Ingresada No esta Disponible...")
            op = int(input("Ingrese Nuevamente Su Opcion: "))
            
        if op == 1:
            print("\n---- Enviando SMS :) ----")
            side = data['SID']
            Token = data['Token']
            NumATA = data['Numero Local']
            Num = input("\n- Ingresa El Numero de Telefono De Destino (No Olvides El Codigo Internacional): ")
            ob = input(Num +" ¿Es Correcto? (s/n): ")
            while ob == "n":
                print("(No Olvides El Codigo Internacional) ")
                Num = input("\n- Ingresa El Numero de Telefono De Destino Nuevamente: ")
                ob = input(Num," ¿Es Correcto? (s/n): ")
                clear()
            clear()
            print("Numero Destino: ",Num)
            mesg = input("\n-- Ingresa Tu Mensaje: ")
            Sub_Twilio(side, Token, NumATA, Num, mesg)
        elif op == 2:
            print("\n¿Desea Eliminar Su Cuenta Realmente?")
            yes = input("Ingrese SI(y) o NO(n): ")
            if yes == "y" or "Y":
                eliminar_archivo_json(selec)
            else:
                Main()
        else:
            print("Payload Finalizado...")



clear()
print(Fore.BLUE + "*** Iniciando Gestor De SMS *** ")
print(Fore.GREEN + "[!] Verificando Cuentas Registradas...")
reverse(seg=1)
directorio = 'Scritps/cache/Acconts_sms/'
archit = Todas_Cuentas(directorio)
if os.path.exists(directorio):
    if archit:
        print(Fore.CYAN + "\n --- Cuentas Encontradas:")
        x = 1
        for cuentas in archit:
            print("|",x,"|",cuentas)
            Cuentass[x] = cuentas
            x = x + 1
    else:
        print("No se encontraron Cuentas!")
        subprocess.run(['python', 'Scritps/Update/Create_SmS_Twilio.py'])
    x = x - 1
else:
    print(Fore.RED + "[!] Error. No Hay Cuentas Existentes!")

opc = int(input("\nIngresa El Numero de la Cuenta: "))
while (opc <= 0) or (opc > x):
    print("\nError. El Numero Ingresado No corresponde a Ninguna Cuenta...")
    opc = int(input("Ingrese Nuevamente El Numero de la Cuenta: "))
selec = Cuentass[opc]
data = Info_Cuentas(selec)
clear()
print(f"\nLa cuenta seleccionada es: {selec}")
reverse(seg=2)
Barra(desc="\nExtrayendo Datos de la Cuenta")
clear()
Info_Cuentas(selec)
reverse(seg=2)
Main()










