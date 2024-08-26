from tqdm import tqdm
from colorama import init, Fore, Style
import os
import subprocess
import platform
import time
import socket
import threading
import webbrowser

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
    for elemento in tqdm(lista_de_elementos, desc=desc):
        time.sleep(0.1)
init(autoreset=True)
bloq_urls = []
#--------------------------------------------------------------------------------------------------------------
def menuConfigURL(els):
    Logo()
    print(Fore.YELLOW + "+ Lista De URLS Bloqueadas +")
    for x in bloq_urls:
        print(x, end=" - ")

    print(Fore.CYAN + Style.DIM + "\n*** Menu De Opciones ***")
    print(Fore.GREEN + f"[1] {Fore.RESET}Bloquear URL")
    print(Fore.GREEN + f"[2] {Fore.RESET}Desbloquear URL")
    print(Fore.RED + f"[3] {Fore.RESET}Salir")
    Opc = int(input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Elija una opción: "))
    if Opc == 1:
        urlbloq = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a bloquear: ")
        bloq_pag(urlbloq)
        menuConfigURL(els)
    elif Opc == 2:
        urlper = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a desbloquear: ")
        permi_pag(urlper)
        menuConfigURL(els)
    else:
        if els is True:
            Main()

def Create_Cache(data):
    with open(os.path.join(os.path.join("Scritps/allFiles/"), 'HostProxy-Cache.txt'), 'w') as file:
        file.write(data)
def Deleted_Cache():
    if os.path.isfile(os.path.join("Scritps/allFiles/", 'HostProxy-Cache.txt')):
        try:
            os.remove(os.path.join("Scritps/allFiles/", 'HostProxy-Cache.txt'))
        except Exception as e:
            print(f"{Fore.RED}[!] Error al eliminar El Archivo de Version: {e}")

def bloq_pag(urlbloq):
    if urlbloq not in bloq_urls:
        bloq_urls.append(urlbloq)
        print(Fore.RED + f"[!] URL bloqueada: {urlbloq}")
        reverse(seg=0.8)

def permi_pag(urlper):
    if urlper in bloq_urls:
        bloq_urls.remove(urlper)
        print(Fore.GREEN + f"[!] URL desbloqueada: {urlper}")
        reverse(seg=0.8)

def Logo():
    clear()
    VerLocal = 'Scritps/allFiles/HostProxy-Cache.txt'
    print(Fore.BLUE + f"HOSTPROXY - SySTool {Fore.CYAN + Style.DIM}(NesAnTime)")
    try:
        if not os.path.exists(VerLocal):
            print()
        with open(VerLocal, 'r') as file:
            contenido_local = file.read().strip()
            if contenido_local == "Mode Enable - Mode Start Init ... Not Mode Pilot . No Update Pilot --- Start INIT":
                print(Fore.GREEN + f"Enable Mode: {Style.BRIGHT}Init")
            elif contenido_local == "Mode Enable - Mode Start Pilot ... Not Mode Init . No Update Init --- Start PILOT":
                print(Fore.GREEN + f"Enable Mode: {Style.BRIGHT}Pilot")
    except Exception as e:
        print(f"{Fore.RED}[!] Error al leer el archivo local: {e}")
    print(Fore.RED + "  _    _           _   _____")
    print(Fore.RED + " | |  | |         | | |  __ \\ ")
    print(Fore.RED + " | |__| | ___  ___| |_| |__) | __ _____  ___   _ ")
    print(Fore.RED + " |  __  |/ _ \\/ __| __|  ___/ '__/ _ \\ \\/ / | | |")
    print(Fore.RED + " | |  | | (_) \\__ \\ |_| |   | | | (_) >  <| |_| |")
    print(Fore.RED + " |_|  |_|\\___/|___/\\__|_|   |_|  \\___/_/\\_\\\\__, |")
    print(Fore.RED + "                                            __/ |")
    print(Fore.RED + "                                           |___/")
#------------------------------------------------------------------------------------------------------------
def handle_client(client_socket, bloqueo_urls, file, mode):
    try:
        request = client_socket.recv(1024)
        request_line = request.split(b'\n')[0]
        url = request_line.split(b' ')[1].decode()

        if mode == "init" and file:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n{content}"
            else:
                response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n<h1>404 Not Found</h1><p>El archivo solicitado no se encuentra en el servidor.</p>"
                
            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()
            return

        if any(url.startswith(b) for b in bloqueo_urls):
            client_socket.send(b"HTTP/1.1 403 Forbidden\r\n\r\n")
            client_socket.close()
            return
        
        if b'CONNECT' in request_line:
            webserver, port = url.split(':')
            port = int(port)
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.connect((webserver, port))
            client_socket.send(b"HTTP/1.1 200 Connection established\r\n\r\n")
            client_to_server = threading.Thread(target=forward, args=(client_socket, remote_socket))
            server_to_client = threading.Thread(target=forward, args=(remote_socket, client_socket))
            client_to_server.start()
            server_to_client.start()
            client_to_server.join()
            server_to_client.join()
    except Exception as e:
        print(f"[Error] Ocurrió un error: {e}")
    finally:
        client_socket.close()

def forward(source, destination):
    while True:
        try:
            data = source.recv(4096)
            if len(data) > 0:
                destination.send(data)
            else:
                break
        except Exception as e:
            print(f"[Error] Ocurrió un error al reenviar datos: {e}")
            break

def proxy(ip, port, Init_File="Scritps/allFiles/Host-Proxy/google-login/"):
    VerLocal = 'Scritps/allFiles/HostProxy-Cache.txt'
    try:
        if not os.path.exists(VerLocal):
            print()
        with open(VerLocal, 'r') as file:
            contenido_local = file.read().strip()
            if contenido_local == "Mode Enable - Mode Start Init ... Not Mode Pilot . No Update Pilot --- Start INIT":
                mode = "init"
            elif contenido_local == "Mode Enable - Mode Start Pilot ... Not Mode Init . No Update Init --- Start PILOT":
                mode = "pilot"
    except Exception as e:
        print(f"{Fore.RED}[!] Error al leer el archivo local: {e}")
        
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Proxy escuchando en {ip}:{port}")

    def Urate():
        Uprate = input(Fore.CYAN + f"\n[HostProxy] > {Fore.RESET}")
        if (Uprate == "Log") or (Uprate == "Console") or (Uprate == "console") or (Uprate == "log"):
            try:
                while True:
                    client_socket, addr = server.accept()
                    print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Conexión aceptada de {addr[0]}:{addr[1]}")
                    client_handler = threading.Thread(target=handle_client, args=(client_socket, bloq_urls, Init_File, mode))
                    client_handler.start()
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\n[!] Interrupción del servidor detectada. Volviendo al menú principal...")
                reverse(seg=1)
                Urate()
            finally:
                server.close()
                reverse(seg=1)
        elif (Uprate == "set config") or (Uprate == "Set Config"):
            menuConfigURL(els=False)
            Urate()
        else:
            print(Fore.RED + "[!] Error. Comando Inexistente...")
            input("Presione Enter para Continuar...")
    Urate()

def Main():
    Logo()
    Host = input(Fore.CYAN + f"\n[HostProxy] > {Fore.RESET}")
    if (Host == "set configure") or (Host == "set config") or (Host == "set -c") or (Host == "set -C"):
        print(Fore.GREEN + "[!] Modo De Configuracion habilitado")
        Opt = input(Fore.CYAN + f"\n[HostProxy - Configure] > {Fore.RESET}")
        if (Opt == "set mode init") or (Opt == "Set Mode Init") or (Opt == "Set Mode -I") or (Opt == "set mode -i"):
            Deleted_Cache()
            Create_Cache(data="Mode Enable - Mode Start Init ... Not Mode Pilot . No Update Pilot --- Start INIT")
            Main()

        elif (Opt == "set mode pilot") or (Opt == "Set Mode Pilot") or (Opt == "Set Mode -P") or (Opt == "set mode -p"):
            Deleted_Cache()
            Create_Cache(data="Mode Enable - Mode Start Pilot ... Not Mode Init . No Update Init --- Start PILOT")
            Main()

        elif (Opt == "set mode deleted") or (Opt == "Set Mode Deleted") or (Opt == "set mode none") or (Opt == "Set Mode None"):
            Deleted_Cache()
            Main()

        elif (Opt == "list url") or (Opt == "List Url") or (Opt == "Config Url") or (Opt == "config url") or (Opt == "Configuracion Url") or (Opt == "configuracion url"):
            VerLocal = 'Scritps/allFiles/HostProxy-Cache.txt'
            try:
                if not os.path.exists(VerLocal):
                    print()
                with open(VerLocal, 'r') as file:
                    contenido_local = file.read().strip()
                    if contenido_local == "Mode Enable - Mode Start Init ... Not Mode Pilot . No Update Pilot --- Start INIT":
                        print(Fore.RED + f"[!] El Modo de Operacion: {Style.BRIGHT}Pilot {Style.NORMAL}. Inpide la Accion! ")
                        input(Fore.YELLOW + "Presione Enter para Continuar...")
                        Main() 
                    elif contenido_local == "Mode Enable - Mode Start Pilot ... Not Mode Init . No Update Init --- Start PILOT":
                        menuConfigURL(els=True)
            except Exception as e:
                print(f"{Fore.RED}[!] Error al leer el archivo local: {e}")

        else:
            print(Fore.RED + "[!] Error. Comando Invalido")
            Main()

    elif (Host == "set mode deleted") or (Host == "Set Mode Deleted") or (Host == "set mode none") or (Host == "Set Mode None"):
        Deleted_Cache()
        Main()
   
    elif (Host == "run") or (Host == "start") or (Host == "exploit") or (Host == "Run") or (Host == "Start") or (Host == "Exploit"):
        Logo()
        ip = input(f"{Fore.CYAN}\n[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Su Direccion IP: ")
        Comip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
        while (Comip == "n"):
            ip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
            Comip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
        print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({ip}), ¡Correctamente!")
        reverse(seg=1.5)

        Logo()
        port = int(input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
        print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
        reverse(seg=1.5)
        clear()

        print(Fore.BLUE + "*** ESTABLECIDO ***")
        print(f"{Fore.BLUE + Style.DIM}Direccion IP: {Fore.RESET + ip}")
        print(f"{Fore.BLUE + Style.DIM}PORT: {Fore.RESET + str(port)}")

        reverse(seg=2)
        print(Fore.GREEN + f"[!] Servidor Iniciado ")

        proxy(ip, port)
    
    elif (Host == "help") or (Host == "Help"):
                print("\n---------- ¿Ayuda? Estos Son los Comandos Que Puedes Usar ----------\n")
                print(f"{Style.DIM}{Fore.BLUE}COMANDO: set configure url, set config url, set -c, set -C {Fore.RESET}{Style.RESET_ALL}- Configurar el Despliegue de Host-Proxy")
                print(f"{Style.DIM}{Fore.BLUE}COMANDO: start, run, exploit, Start, Run, Exploit {Fore.RESET}{Style.RESET_ALL}- Iniciar Despliegue de Host-Proxy")
                print(f"{Style.NORMAL}{Fore.BLUE}¿Mas Informacion Sobre Este Tools? {Fore.RESET}{Style.BRIGHT} COMANDO: {Style.NORMAL} Help_Tool, helptool")
                print(f"{Style.DIM}{Fore.YELLOW}COMANDO: Exit, exit {Fore.RESET}{Style.RESET_ALL} - Atras\n")
                input(Fore.YELLOW + "\nPresione Enter Para Continuar...")
                Main()

    elif (Host == "Help_Tool") or (Host == "helptool"):
        webbrowser.open()
    
    else:
        print(Fore.RED + "[!] Error. Comando Invalido")
        input("Presione Enter para Continuar...")
        Main()

Main()