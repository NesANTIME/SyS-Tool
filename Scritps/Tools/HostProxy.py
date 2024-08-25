from tqdm import tqdm
from colorama import init, Fore, Style
import os
import subprocess
import platform
import time
import socket
import threading

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
    for elemento in tqdm(lista_de_elementos, desc=desc):  # Corregido
        time.sleep(0.1)

init(autoreset=True)
inicit = 0
bloqueo_urls = []

def Logo():
    global inicit
    print(Fore.BLUE + f"HOSTPROXY - SySTool {Fore.CYAN + Style.DIM}(NesAnTime)")
    if inicit == 0:
        print()
    elif inicit == 1:
        print(Fore.GREEN + f"Enable Mode: {Style.BRIGHT}Pilot")
    elif inicit == 2:
        print(Fore.GREEN + f"Enable Mode: {Style.BRIGHT}Init")
    print(Fore.RED + "  _    _           _   _____")
    print(Fore.RED + " | |  | |         | | |  __ \\ ")
    print(Fore.RED + " | |__| | ___  ___| |_| |__) | __ _____  ___   _ ")
    print(Fore.RED + " |  __  |/ _ \\/ __| __|  ___/ '__/ _ \\ \\/ / | | |")
    print(Fore.RED + " | |  | | (_) \\__ \\ |_| |   | | | (_) >  <| |_| |")
    print(Fore.RED + " |_|  |_|\\___/|___/\\__|_|   |_|  \\___/_/\\_\\\\__, |")
    print(Fore.RED + "                                            __/ |")
    print(Fore.RED + "                                           |___/")

def bloquear_pagina(urlbloq):
    global inicit
    if urlbloq not in bloqueo_urls:
        bloqueo_urls.append(urlbloq)
        print(Fore.RED + f"[!] URL bloqueada: {urlbloq}")
        inicit = 1
        reverse(seg=0.8)

def permitir_pagina(urlper):
    if urlper in bloqueo_urls:
        bloqueo_urls.remove(urlper)
        print(Fore.GREEN + f"[!] URL desbloqueada: {urlper}")
        reverse(seg=0.8)

def handle_client(client_socket, bloqueo_urls, file=None):
    global inicit
    try:
        request = client_socket.recv(1024)
        request_line = request.split(b'\n')[0]
        url = request_line.split(b' ')[1].decode()

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
        else:
            if inicit == 2 and file:
                if os.path.exists(file):
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n{content}"
                else:
                    response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n<h1>404 Not Found</h1><p>El archivo solicitado no se encuentra en el servidor.</p>"
                    
                client_socket.sendall(response.encode('utf-8'))
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

def proxy(ip, port, file=None):
    global inicit
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Proxy escuchando en {ip}:{port}")
    
    try:
        while True:
            client_socket, addr = server.accept()
            print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Conexión aceptada de {addr[0]}:{addr[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, bloqueo_urls, file))
            client_handler.start()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Interrupción del servidor detectada. Volviendo al menú principal...")
        reverse(seg=1)
        Main() 
    finally:
        server.close()
        reverse(seg=1)

def Main():
    global inicit
    clear()
    Logo()
    Host = input(Fore.CYAN + f"\n[HostProxy] > {Fore.RESET}")
    if (Host == "set configure") or (Host == "set config"):
        def menuConfig():
            clear()
            Logo()
            print(Fore.YELLOW + "+ Lista De URLS Bloqueadas +")
            for x in bloqueo_urls:
                print(x, end=" - ")

            print(Fore.CYAN + Style.DIM + "\n*** Menu De Opciones ***")
            print(Fore.GREEN + f"[1] {Fore.RESET}Bloquear URL")
            print(Fore.GREEN + f"[2] {Fore.RESET}Desbloquear URL")
            print(Fore.RED + f"[3] {Fore.RESET}Salir")
            Yet = int(input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Elija una opción: "))
            if Yet == 1:
                urlbloq = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a bloquear: ")
                bloquear_pagina(urlbloq)
                menuConfig()
            elif Yet == 2:
                urlper = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a desbloquear: ")
                permitir_pagina(urlper)
                menuConfig()
            else:
                Main()
        menuConfig()

    elif (Host == "run") or (Host == "start") or (Host == "exploit"):
        clear()
        Logo()
        ip = input(f"{Fore.CYAN}\n[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Su Direccion IP: ")
        opb = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
        while (opb == "n"):
            ip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
            opb = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
        print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({ip}), ¡Correctamente!")
        reverse(seg=1.5)
        clear()

        Logo()
        port = int(input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
        print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
        reverse(seg=1.5)
        clear()

        if inicit == 2:
            print("Añada la Ruta del Html")
            file = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET} Ingrese la ruta al archivo HTML: ")
        else:
            file = None

        print(Fore.BLUE + "*** ESTABLECIDO ***")
        print(f"{Fore.BLUE + Style.DIM}Direccion IP: {Fore.RESET + ip}")
        print(f"{Fore.BLUE + Style.DIM}PORT: {Fore.RESET + str(port)}")

        reverse(seg=2)
        print(Fore.GREEN + f"[!] Servidor Iniciado ")

        proxy(ip, port, file)
    
    elif (Host == "help"):
        print()  

    elif (Host == "set mode pilot") or (Host == "Set Mode Pilot"):
        inicit = 1
        Main()
    elif (Host == "set mode init") or (Host == "Set Mode Init"):
        inicit = 2
        Main()
Main()
