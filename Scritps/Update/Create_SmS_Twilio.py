#Creado Por NeAnTime, Modulos Para Sofware Principal
from colorama import init, Fore, Style
from twilio.rest import Client
from tqdm import tqdm
import webbrowser
import subprocess
import platform
import random
import string
import time
import json
import os

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
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------------

def Save_Acconts(sid, Token, NumATA):
    clear()
    filPact = os.path.join(carpeta, 'SMS_Twilio.txt')
    print(Fore.GREEN + "[!] A Continuacion se Guardara Tu Cuenta de Manera Local")
    print("Para Que la Proxima Vez No Vuelvas A Ingresar Informacion\n")
    nombre = input("Ingresa Un Nombre Para La Cuenta: ")

    data = {'nombre': nombre, 'SID': sid, 'Token': Token, 'Numero Local': NumATA, "Tipo_Cuenta:": "Twilio"}
    carpeta = 'Scritps/allFiles/Acconts-SMS/'
    filt = nombre + '.json'
    rut = os.path.join(carpeta, filt)

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(rut, 'w') as file:
        json.dump(data, file)
    
    reverse(seg=1)
    print(Fore.GREEN + "[!] Cuenta Creada Exitosamente...")
    print(f"Datos guardados en {rut}")
    
    with open(filPact, 'w') as file:
        cadent = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        file.write(cadent)
    reverse(seg=2)
    subprocess.run(['python', 'Scritps/Tools/SmSTwilio.py'])


def funcion(sid, Token, NumATA):
    clear()
    print(Fore.CYAN + "[+] Datos Ingresados [+]\n")
    print(f"{Style.BRIGHT + Fore.GREEN}-- SID:{Style.NORMAL + Fore.RESET} {sid}")
    print(f"{Style.NORMAL + Fore.GREEN}-- Token:{Style.NORMAL + Fore.RESET} {Token}")
    print(f"{Fore.GREEN}-- Tu Numero:{Style.NORMAL + Fore.RESET} {NumATA}")
    print(Fore.RED + "\n[!] A Continuacion se realizara una prueba, con los datos Ingresados...")
    print("\nIngresa Un Numero De Telefono para Recibir El Texto de Prueba (El Numero de Destino debe Contener el codigo Internacional)")
    print(Fore.YELLOW + "[?] Si No conoces tu Numero Internacional, coloca un # ")
    numVIC = input(f"{Fore.YELLOW}-- {Fore.RESET}Ingresa El Numero: ")
    if numVIC == "#":
        print(Fore.GREEN + "\n[!] Se Abrira El Navegador! ")
        reverse(seg=2)
        webbrowser.open("https://www.dialapplet.com/prefijos-telefonicos-internacionales/")
        funcion()
    clear()

    client = Client(sid, Token)
    message = client.messages.create(
        body="* SySTooL - SMS TWILIO... Esto es un Mensaje De Prueba, Verifica Que la Herramienta Funcione Sin Errores! ",
        from_=NumATA,
        to=numVIC
        )
    print(Fore.GREEN + f"[!] El Fue Mensaje enviado: {message.sid}")
    reverse(seg=1)
    Save_Acconts(sid, Token, NumATA)


clear()
print(Fore.CYAN + Style.DIM + " {+} SySTool - Nesantime {+} ")
print(Fore.BLUE + "*** Creador de Cuentas Locales SMS desde Twilio ***")
sid = input(f"\n- Ingresa tu SID {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Style.BRIGHT + Fore.GREEN} ")
Token = input(f"{Style.NORMAL + Fore.RESET}-- Ingresa Tu Token {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Style.NORMAL + Fore.GREEN} ")
NumATA = int(input(f"{Style.NORMAL + Fore.RESET}--- Ingresa Tu Numero {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Fore.GREEN} "))

opc = input(Fore.GREEN + Style.NORMAL + f"\n[!] ¿Todos los Datos Ingresados Son Correctos? (s/n):{Style.NORMAL + Fore.RESET} ")
while opc == "n":
    sid = input(f"\n- Ingresa Nuevamente tu SID {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Style.BRIGHT + Fore.GREEN} ")
    Token = input(f"{Style.NORMAL + Fore.RESET}-- Ingresa Nuevamente Tu Token {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Style.NORMAL + Fore.GREEN} ")
    NumATA = int(input(f"{Style.NORMAL + Fore.RESET}--- Ingresa Nuevamente Tu Numero {Fore.YELLOW + Style.DIM}(Mostrada En Twilio):{Fore.GREEN} "))
    opc = input(Fore.GREEN + Style.NORMAL + f"\n[!] ¿Todos los Datos Ingresados Son Correctos? (s/n):{Style.NORMAL + Fore.RESET} ")
funcion(sid, Token, NumATA)
