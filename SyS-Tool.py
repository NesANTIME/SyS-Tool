#Programa Creado Por NesAnTime
from tqdm import tqdm
from colorama import init, Fore, Style
import os
import subprocess
import platform
import time
import argparse

#----------------------------------------------------------------
Version = "SyS-Tool - NesAnTime (Version 3.0)"
#-----------------------------------------------------------------
def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(40)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
def New_Update_create():
    reverse(seg=1)
    with open(os.path.join('Scritps/allFiles/', 'NewUpdate.txt'), 'r') as archivo:
        contenid = archivo.read()
        return contenid
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
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------------
def Opc_APK():
    clear()
    subprocess.run(['python', 'Scritps/Tools/CreateAndroid.py'])

def Opc_EXE():
    clear()
    subprocess.run(['python', 'Scritps/Tools/CreateEXE.py'])

def Opc_HostProxy():
    clear()
    subprocess.run(["python", "Scritps/Tools/HostProxy.py"])

#_____________________________________________________________________________________________________________
def Update():
    subprocess.run(['python', 'Scritps/Update/Update.py'])
    if os.path.exists(os.path.join('Scritps/allFiles/', 'NewUpdate.txt')):
        return True
    else:
        return False
    
def Start():
    clear()
    reverse(seg=0.2)
    print(f"{Fore.BLUE}[+] {Fore.RESET}INiciando.")
    reverse(seg=0.3)
    clear()
    print(f"{Fore.BLUE}[×] {Fore.RESET}inICiando..")
    reverse(seg=0.3)
    clear()
    print(f"{Fore.BLUE}[+] {Fore.RESET}inicIAndo...")
    reverse(seg=0.3)
    clear()
    print(f"{Fore.BLUE}[×] {Fore.RESET}iniciaNDo....")
    reverse(seg=0.3)
    clear()
    print(f"{Fore.BLUE}[+] {Fore.RESET}iniciandO....")
    reverse(seg=0.3)
    clear()

    Barra(desc="Analizando Paquetes ")
    rut = os.path.join('Scritps/allFiles/', 'Execute.txt')
    with open('Scritps/allFiles/Install.txt', 'w') as file:
        file.write(Version)
    Update()

    if os.path.exists(rut):
        print(Fore.GREEN + "[!] Paquetes existentes, Herramienta Sin Errores!")
        reverse(seg=1)
        with open(rut, 'r') as f:
            if not Update():
                Vert = "\n"
            else:
                Vert = f"{New_Update_create()}\n"
            Main(Vert)
    else:
        print(Fore.RED + "\n[!] La Herramienta se a ejecutado por primera vez...")
        print("Se Realizara Una Comprobacion de las Dependencias del Dispositivo...")
        input(Fore.YELLOW + "Presione Enter Para Continuar... ")
        subprocess.run(['python', 'Scritps/Update/Depend_Update.py'])
        Start()



def Main(Vert):
    clear()
    Logo()
    print(f"\n {Style.DIM}{Version}")
    print(f"{Fore.GREEN}{Vert}")

    print(f"{Style.BRIGHT}{Fore.BLUE}__________ Menu De Opciones __________")
    print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL}Create Payloads ")
    print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL}Ingeneria Social ")
    print(f"{Style.DIM}{Fore.BLUE}[3] {Fore.RESET}{Style.RESET_ALL}¿Ayuda?")
    print(f"\n{Style.DIM}{Fore.BLUE}[4] {Fore.RESET}{Style.RESET_ALL}Cerrar SysTool")
    opc = int(input(f"\n{Fore.YELLOW}-- {Fore.RESET}Ingrese La Opcion: "))
    while (opc < 1) or (opc > 4):
        print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
        opc = int(input(f"{Fore.YELLOW}-- {Fore.RESET}Ingrese Nuevamente La Opcion: "))

    if (opc == 1):
        def OPC1():
            clear()
            Logo()
            print(f"\n{Style.BRIGHT}{Fore.BLUE}Ingeneria Inversa - Creacion de Software (Basico)\n")
            Escrip = input(f"{Style.BRIGHT}[Ingeneria Inversa - SySTool] > {Style.NORMAL}")
        
            if (Escrip == "Create APK") or (Escrip == "Create Apk") or (Escrip == "create apk") or (Escrip == "create -a") or (Escrip == "Create -A"):
                Opc_APK()
            elif (Escrip == "Create EXE") or (Escrip == "Create Exe") or (Escrip == "create exe") or (Escrip == "create -e") or (Escrip == "Create -E"):
                Opc_EXE()
            elif (Escrip == "help") or (Escrip == "Help"):
                print("\n---------- ¿Ayuda? Estos Son los Comandos Que Puedes Usar ----------\n")
                print(f"{Style.DIM}{Fore.BLUE}COMANDO: {Style.NORMAL}create apk, Create APK, Create Apk, create -a, Create -A {Fore.RESET}{Style.RESET_ALL}- Crear Archivo (.Apk)")
                print(f"{Style.DIM}{Fore.BLUE}COMANDO: {Style.NORMAL}create exe, Create EXE, Create Exe, create -e, Create -E {Fore.RESET}{Style.RESET_ALL}- Crear Archivo (.Exe)")
                print(f"{Style.DIM}{Fore.YELLOW}COMANDO: {Style.NORMAL}Exit, exit {Fore.RESET}{Style.RESET_ALL} - Atras\n")
                input(Fore.YELLOW + "\nPresione Enter Para Continuar...")
                OPC1()
            elif (Escrip == "Exit") or (Escrip == "exit"):
                Main(Vert)
            else:
                print(Fore.RED + "[!] Error. El Comando ("+ Escrip +") NO esta Disponible o NO Existe :(")
                print("Si Tienes Alguna Duda O Nesecitas Ayuda, Usa el Comando Help")
                input(Fore.YELLOW + "\nPresione Enter Para Continuar...")
                OPC1()
        OPC1()

    elif (opc == 2):
        def OPC2():
            clear()
            Logo()
            print(f"\n{Style.BRIGHT}{Fore.BLUE}Tools de Ingeneria Social (Version 2.0)\n")
            Escrip2 = input(f"{Style.BRIGHT}[Ingeneria Inversa - SySTool] > {Style.NORMAL}")
        
            if (Escrip2 == "H Proxy") or (Escrip2 == "h proxy") or (Escrip2 == "HostProxy") or (Escrip2 == "hostproxy") or (Escrip2 == "HProxy") or (Escrip2 == "hproxy"):
                Opc_HostProxy()
            elif (Escrip2 == "help") or (Escrip2 == "Help"):
                print("\n---------- ¿Ayuda? Estos Son los Comandos Que Puedes Usar ----------\n")
                print(f"{Style.DIM}{Fore.BLUE}COMANDO: H Proxy, h proxy, HostProxy, hostproxy, HProxy, hproxy {Fore.RESET}{Style.RESET_ALL}- Cargar Tool Host-Proxy")
                print(f"{Style.NORMAL}{Fore.BLUE}¿Mas Informacion Sobre Nuestros Tools? {Fore.RESET}{Style.BRIGHT} COMANDO: {Style.NORMAL} Help Tool, help tool")
                print(f"{Style.DIM}{Fore.YELLOW}COMANDO: Exit, exit {Fore.RESET}{Style.RESET_ALL} - Atras\n")
                input(Fore.YELLOW + "\nPresione Enter Para Continuar...")
                OPC2()
            elif (Escrip2 == "Exit") or (Escrip2 == "exit"):
                Main(Vert)
            else:
                print(Fore.RED + "[!] Error. El Comando ("+ Escrip2 +") NO esta Disponible o NO Existe :(")
                print("Si Tienes Alguna Duda O Nesecitas Ayuda, Usa el Comando Help")
                input(Fore.YELLOW + "\nPresione Enter Para Continuar...")
                OPC2()
        OPC2()

    else:
        print(Fore.GREEN + "[!] Programa ha Sido Cerrado ")
        reverse(seg=2)
   
Start()