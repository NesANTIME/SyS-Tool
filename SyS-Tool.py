#Programa Creado Por NesAnTime
from tqdm import tqdm
from colorama import init, Fore, Style
import os
import subprocess
import platform
import time
import webbrowser

#----------------------------------------------------------------
Version = "SyS-Tool - NesAnTime (Version 2.0)"
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
def job():
    with open(os.path.join('Scritps/allFiles/', 'NewUpdate.txt'), 'r') as archivo:
        contenid = archivo.read()
        return contenid
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------------
def Opc_Twilio():
    print(f"\n{Fore.GREEN}{Style.DIM}[!] Comprobando Existencia De Cuentas! ")
    reverse(seg=1)
    ruta_txt = os.path.join('Scritps/allFiles/', 'SMS_Twilio.txt')
    if os.path.exists(ruta_txt):
        print(Fore.GREEN + "[!] Cuentas ¡Existentes!")
        reverse(seg=1)
        with open(ruta_txt, 'r') as f:
            clear()
            reverse(seg=1.5)
            subprocess.run(['python', 'Scritps/Tools/SmSTwilio.py'])
    else:
        print(Fore.RED + "\n[!] ¡No se Encontro Ninguna Cuenta Existente! ")
        print("A continuacion, Debera Registrar Una Cuenta API a Ultilizar...")
        reverse(seg=1.5)
        subprocess.run(['python', 'Scritps/Update/Create_SmS_Twilio.py'])

def Opc_APK():
    clear()
    subprocess.run(['python', 'Scritps/Tools/CreateAndroid.py'])

def Opc_BAT():
    clear()
    subprocess.run(['python', 'Scritps/Tools/CreateBAT.py'])


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
                Vert = f"{job()}\n"
            Main(Vert)
    else:
        print(Fore.RED + "\n[!] La Herramienta se a ejecutado por primera vez...")
        print("Se Realizara Una Comprobacion de las Dependencias del Dispositivo...")
        input(Fore.YELLOW + "Presione Enter Para Continuar... ")
        subprocess.run(['python', 'Scritps/Update/Depend_Update.py'])
        Start()



def Main(Vert):
    clear()
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
    print(f"\n {Style.DIM}{Version}")
    print(f"{Fore.GREEN}{Vert}")

    print(f"{Style.BRIGHT}{Fore.BLUE}__________ Menu De Opciones __________")
    print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL}Ingeneria Inversa (Reverb Shell, Tools)")
    print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL}Ingeneria Social (SMS, CORREOS)")
    print(f"{Style.DIM}{Fore.BLUE}[3] {Fore.RESET}{Style.RESET_ALL}Cerrar Sysnes")
    opc = int(input(f"\n{Fore.YELLOW}-- {Fore.RESET}Ingrese La Opcion: "))
    while (opc < 1) or (opc > 3):
        print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
        opc = int(input(f"{Fore.YELLOW}-- {Fore.RESET}Ingrese Nuevamente La Opcion: "))

    if (opc == 1):
        clear()
        print(f"\n{Style.BRIGHT}{Fore.BLUE}Ingeneria Inversa - Creacion de Software (Basico)")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL}- Crear Archivo (.Apk)")
        print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL}- Crear Archivo (.bat)")
        print(f"{Style.DIM}{Fore.YELLOW}[99] {Fore.RESET}{Style.RESET_ALL} - Atras\n")
        opc1 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese La Opcion: "))
        if opc1 == 99:
            Main(Vert)
        else:
            while (opc1 < 1) or (opc1 > 2):
                print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
                opc1 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese Nuevamente La Opcion: "))

            if opc1 == 1:
                Opc_APK()
            elif opc1 == 2:
                Opc_BAT()

    elif (opc == 2):
        clear()
        print(f"\n{Style.BRIGHT}{Fore.BLUE}Ingeneria Social (Version 1.2)\n")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print(f"{Style.DIM}{Fore.BLUE}[1] {Fore.RESET}{Style.RESET_ALL}Enviar SMS...")
        print(f"{Style.DIM}{Fore.BLUE}[2] {Fore.RESET}{Style.RESET_ALL}Enviar Correos...")
        print(f"{Style.DIM}{Fore.YELLOW}[99] {Fore.RESET}{Style.RESET_ALL} - Atras\n")
        opc2 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese La Opcion: "))
        if opc2 == 99:
            Main(Vert)
        else:
            while (opc2 < 1) or (opc2 > 2):
                print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
                opc2 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese Nuevamente La Opcion: "))
            
            if opc2 == 1:
                clear()
                print(f"\n{Style.BRIGHT}{Fore.BLUE}Ingeneria Social (Version 1.2)\n")
                print(Fore.CYAN + Style.DIM + "¿ Enviar SMS ?\n")
                print("-- La Herramienta Es Compatible Solo Con los Siguientes Servicios SMS: \n")
                print(f"{Style.DIM}{Fore.BLUE}   [1] {Fore.RESET}{Style.RESET_ALL}Twilio (Debe Tener Una Cuenta En esta Plataforma)")
                print(f"{Style.DIM}{Fore.YELLOW}   [99] {Fore.RESET}{Style.RESET_ALL} - Atras\n")
                opc3 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese La Opcion: "))
                if opc3 == 99:
                    Main(Vert)
                else:
                    while (opc3 < 1) or (opc3 > 1):
                        print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
                        opc3 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese Nuevamente La Opcion: "))
                    
                    if opc3 == 1:
                        clear()
                        Opc_Twilio()
                
            elif opc2 == 2:
                clear()
                print(f"\n{Style.BRIGHT}{Fore.BLUE}Ingeneria Social (Version 1.2)\n")
                print(Fore.CYAN + Style.DIM + "¿ Enviar Correos ?\n")
                print("-- La Herramienta Es Compatible Solo Con los Siguientes Servicios De Correo: \n")
                print(f"{Style.DIM}{Fore.BLUE}   [1] {Fore.RESET}{Style.RESET_ALL}Proton.me (Debe Tener Una Cuenta En esta Plataforma)")
                print(f"{Style.DIM}{Fore.YELLOW}   [99] {Fore.RESET}{Style.RESET_ALL} - Atras\n")
                opc4 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese La Opcion: "))
                if opc4 == 99:
                    Main(Vert)
                else:
                    while (opc4 < 1) or (opc4 > 1):
                        print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
                        opc4 = int(input(f"{Fore.YELLOW}--- {Fore.RESET}Ingrese Nuevamente La Opcion: "))
                    
                    if opc4 == 1:
                        clear()
                        print(Fore.GREEN + "[!] Se va Abrir La Web Oficial De Proton.me")
                        reverse(seg=2)
                        webbrowser.open("https://proton.me/")
                        input(Fore.YELLOW + "Presione Enter para Continuar...")
    
    else:
        print(Fore.GREEN + "[!] Programa ha Sido Cerrado ")
        reverse(seg=2)
   

Start()