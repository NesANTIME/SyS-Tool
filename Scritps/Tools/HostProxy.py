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
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
init(autoreset=True)
# -------------------------------------------------------------------------------
bloqueo_urls = []

def bloquear_pagina(url):
    if url not in bloqueo_urls:
        bloqueo_urls.append(url)
        print(Fore.RED + f"[!] URL bloqueada: {url}")
        reverse(seg=0.8)
def permitir_pagina(url):
    if url in bloqueo_urls:
        bloqueo_urls.remove(url)
        print(Fore.GREEN + f"[!] URL desbloqueada: {url}")
        reverse(seg=0.8)

def handle_client(client_socket):
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

def proxy(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Proxy escuchando en {ip}:{port}")
    try:
        while True:
            client_socket, addr = server.accept()
            print(Fore.GREEN + Style.BRIGHT + f"[SYS-HostProxy] {Style.NORMAL}Conexión aceptada de {addr[0]}:{addr[1]}")
            
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Interrupción del servidor detectada. Volviendo al menú principal...")
        reverse(seg=1)
        Main()
    finally:
        server.close()
        reverse(seg=1)
        Main()

def Main():
    clear()
    print(Fore.BLUE + f"HOSTPROXY - SySTool {Fore.CYAN + Style.DIM}(NesAnTime)\n")
    print(Fore.CYAN + "*** Menu De Opciones ***")
    print(Fore.GREEN + f"[1] {Fore.RESET}Administar Acceso a páginas ")
    print(Fore.GREEN + f"\n[Start - Run - Exploit] Iniciar proxy")
    print(Fore.RED + f"[99] Salir\n")
    opc = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Elija una opción: ")
    if opc == 99:
        Main()
    else:
        while (opc < 1) or (opc > 1):
            print(Fore.RED + "[!] Error. La Opcion No esta Disponible :(")
            opc = int(input(f"{Fore.YELLOW}-- {Fore.RESET}Ingrese Nuevamente La Opcion: "))

        if opc == 1:
            clear()
            print(bloqueo_urls, end=" ")
            print(Fore.CYAN + Style.DIM + "\n*** Menu De Opciones ***")
            print(Fore.GREEN + f"[1] {Fore.RESET}Bloquear URL")
            print(Fore.GREEN + f"[2] {Fore.RESET}Desbloquear URL")
            print(Fore.RED + f"[3] {Fore.RESET}Salir")
            opc1 = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Elija una opción: ")
            if opc1 == 1:
                urlbloq = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a bloquear: ")
                bloquear_pagina(urlbloq)
            elif opc1 == 2:
                urlper = input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET} Ingrese la URL a desbloquear: ")
                permitir_pagina(urlper)
            else:
                Main()
        
        elif opc == "start" or opc == "Start" or opc == "Run" or opc == "run" or opc == "Exploit" or opc == "exploit":
            clear()
            print(Fore.BLUE + f"HOSTPROXY - SySTool {Fore.CYAN + Style.DIM}(NesAnTime)\n")

            ip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Su Direccion IP: ")
            opb = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
            while (opb == "n"):
                ip = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}Ingrese Nuevamente Su Direccion IP: ")
                opb = input(f"{Fore.CYAN}[SYS-HostProxy] {Fore.RESET + Fore.MAGENTA}- [!] {Fore.RESET}La Direccion IP {Fore.CYAN + ip + Fore.RESET}, Ingresada ¿Es Correcta? (y/n): ")
            print(Fore.GREEN + f"[!] Se Ha Establecido Tu Direccion IP ({ip}), ¡Correctamente!")
            reverse(seg=1.5)
            clear()

            print(Fore.BLUE + f"HOSTPROXY - SySTool {Fore.CYAN + Style.DIM}(NesAnTime)\n")
            port = int(input(f"{Fore.CYAN}[SYS-HostProxy]{Fore.RESET + Fore.MAGENTA} --{Fore.RESET} Proporcione un Puerto de Escucha: "))
            print(Fore.GREEN + f"[!] El Puerto de Escucha ({str(port)}) Se ha Establecido Correctamente..\n")
            reverse(seg=1.5)
            clear()

            print(Fore.BLUE + "*** ESTABLECIDO ***")
            print(f"{Fore.BLUE + Style.DIM}Direccion IP: {Fore.RESET + ip}")
            print(f"{Fore.BLUE + Style.DIM}PORT: {Fore.RESET + str(port)}")
            proxy(ip, port)

Main()