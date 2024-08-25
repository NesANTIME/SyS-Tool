#Creado Por NeAnTime, Modulos Para Sofware Principal
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys
from colorama import init, Fore, Style
import random
import string

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(20)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
init(autoreset=True)
#____________________________________________________________________________________________________
def create_txt():
    file_path = os.path.join(os.path.join("Scritps/allFiles/"), 'Execute.txt')
    with open(file_path, 'w') as file:
        caden = ''.join(random.choices(string.ascii_letters + string.digits, k=90))
        file.write(caden + "- SySTool.Nesantime ")

create_txt()