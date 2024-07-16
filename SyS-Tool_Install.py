#Programa Creado Por NesAnTime
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
#-------------------------------------------------------------------------------------------------------------
def Opc_Twilio():
    archivo_txt = 'SMS_Twilio.txt'
    ruta_txt = os.path.join('Scritps/allFiles/', archivo_txt)
    if os.path.exists(ruta_txt):
        print(f"\nComprobando Existencia De Cuentas en ({archivo_txt})")
        reverse(seg=2)
        print(f"Cuentas en {archivo_txt} ¡Existentes!")
        reverse(seg=1)
        with open(ruta_txt, 'r') as f:
            clear()
            reverse(seg=3)
            subprocess.run(['python', 'Scritps/Tools/SmSTwilio.py'])
    else:
        print(f"\nNo se Encontro la Existencia del archivo {archivo_txt}")
        print("A continuacion, Debera Registrar Una Cuenta API a Ultilizar...")
        reverse(seg=3)
        subprocess.run(['python', 'Scritps/Update/Create_SmS_Twilio.py'])


#_____________________________________________________________________________________________________________
def Update():
    clear()
    subprocess.run(['python', 'Scritps/Update/Update.py'])


def Start():
    clear()
    reverse(seg=0.2)
    print("INiciando.")
    reverse(seg=0.5)
    clear()
    print("inICiando..")
    reverse(seg=0.5)
    clear()
    print("inicIAndo...")
    reverse(seg=0.5)
    clear()
    print("iniciaNDo....")
    reverse(seg=0.5)
    clear()
    print("iniciandO....")
    reverse(seg=0.5)
    clear()

    archivo_txt = 'Execute.txt'
    ruta_txt = os.path.join('Scritps/allFiles/', archivo_txt)

    Barra(desc="Analizando Paquetes...")

    if os.path.exists(ruta_txt):
        print("\nPaquetes existentes, Herramienta Sin Errores!")
        reverse(seg=2)
        with open(ruta_txt, 'r') as f:
            Main()

    else:
        print("\nLa Herramienta se a ejecutado por primera vez...")
        print("Se Realizara Una Comprobacion de las Dependencias del Dispositivo...")
        reverse(seg=3)
        subprocess.run(['python', 'Scritps/Update/Depend_Update.py'])
        Start()



def Main():
    clear()
    print("\nPyload Creado Por NesAnTime\n")
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
    print("\n SyS-Tool - NesAnTime (Version 1.5)\n")

    print("__________ Menu De Opciones __________")
    print("[1] Ingeneria Inversa (Reverb Shell, Tools)")
    print("[2] Ingeneria Social (SMS, CORREOS)")
    print("[3] Cerrar Sysnes")
    print("----------------------------------------------")
    print("[99] Update SysTool")
    
    opc = int(input("\n-- Ingrese La Opcion: "))
    while (opc < 1) or (opc > 3):
        print("Error. La Opcion No esta Disponible :(")
        opc = int(input("-- Ingrese Nuevamente La Opcion: "))

    if (opc == 1):
        clear()
        print("\n Ingeneria Inversa - Creacion de Software (Basico)")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print("[1] - Crear Archivo (.Apk)")
        print("[2] - Crear Archivo (.bat)")
        print("[99] - Atras\n")
        opc1 = int(input("--- Ingrese La Opcion: "))
        if opc1 == 99:
            Main()
        else:
            while (opc1 < 1) or (opc1 > 2):
                print("Error. La Opcion No esta Disponible :(")
                opc1 = int(input("--- Ingrese Nuevamente La Opcion: "))

            if opc1 == 1:
                clear()
                #Añadir Funcion
            elif opc1 == 2:
                clear()
                #Añadir Funcion

    elif (opc == 2):
        clear()
        print("\nIngeneria Social (Version 1.2)\n")
        print("[1] Enviar SMS...")
        print("[2] Enviar Correos...")
        print("[99] Atras..")
        opc2 = int(input("Elija Una de Las SubCategorias: "))
        if opc2 == 99:
            Main()
        else:
            while (opc2 < 1) or (opc2 > 2):
                print("Error. La Opcion No esta Disponible :(")
                opc2 = int(input("--- Ingrese Nuevamente La Opcion: "))
            
            if opc2 == 1:
                clear()
                print("Ingeneria Social (Version 1.2)")
                print("Enviar SMS...\n")
                print("-- La Herramienta Es Compatible Solo Con los Siguientes Servicios SMS: \n")
                print("   [1] Twilio (Debe Tener Una Cuenta En esta Plataforma)")
                print("   [99] Atras..")
                opc3 = int(input("Elija Una de Las SubCategorias: "))
                if opc3 == 99:
                    Main()
                else:
                    while (opc3 < 1) or (opc3 > 1):
                        print("Error. La Opcion No esta Disponible :(")
                        opc3 = int(input("--- Ingrese Nuevamente La Opcion: "))
                    
                    if opc3 == 1:
                        clear()
                        Opc_Twilio()
                
            elif opc2 == 2:
                clear()
                print("Ingeneria Social (Version 1.2)")
                print("Enviar Correos...\n")
                print("-- La Herramienta Es Compatible Solo Con los Siguientes Servicios De Correo: \n")
                print("   [1] Proton.me (Debe Tener Una Cuenta En esta Plataforma)")
                print("   [99] Atras..\n")
                opc4 = int(input("--- Ingrese La Opcion: "))
                if opc4 == 99:
                    Main()
                else:
                    while (opc4 < 1) or (opc4 > 1):
                        print("Error. La Opcion No esta Disponible :(")
                        opc4 = int(input("--- Ingrese Nuevamente La Opcion: "))
                    
                    if opc2 == 1:
                        clear()
                        #Ingresa Su Funcion
    
    elif opc == 99:
        Update()
    else:
        print("Programa ha Sido Cerrado ")
        reverse(seg=2)
   

Start()