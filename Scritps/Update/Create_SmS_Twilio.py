#Creado Por NeAnTime, Modulos Para Sofware Principal
from twilio.rest import Client
from tqdm import tqdm
import subprocess
import platform
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

#-------------------------------------------------------------------------------------------------------------

def save_Cuenta(side, Token, NumATA):
    clear()
    print("\nA Continuacion se Guardara Tu Cuenta de Manera Local, Para Que la Proxima Vez No Vuelvas A Ingresar Informacion\n")
    nombre = input("Ingresa Un Nombre Para La Cuenta: ")

    tip = "Twilio"
    data = {'nombre': nombre, 'SID': side, 'Token': Token, 'Numero Local': NumATA, 'Tipo_Cuenta': tip}
    carpeta = 'Scritps/allFiles/Acconts-SMS/'
    archivo = nombre + '_(Twilio).json'
    rut = os.path.join(carpeta, archivo)

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    with open(rut, 'w') as file:
        json.dump(data, file)
    
    reverse(seg=1)
    print("Cuenta Creada Exitosamente...")
    print(f"Datos guardados en {rut}")

    file_path = os.path.join(carpeta, 'SMS_Twilio.txt')
    with open(file_path, 'w') as file:
        file.write("Text-Cuentas-Cache")
    print(f"\nArchivo de Registro y cache ({archivo}) creado ¡exitosamente!")
    reverse(seg=3)
    subprocess.run(['python', 'Scritps/Tools/SmSTwilio.py'])


def SubMain(side, Token, NumATA, numVIC):
    client = Client(side, Token)
    message = client.messages.create(
        body="Esto es Un Mensaje de Prueba, Responde Si lo has Recibido... SYSNES SMS",
        from_=NumATA,
        to=numVIC
        )
    print(f"El Fue Mensaje enviado: {message.sid}")
    reverse(seg=2)
    side = side
    Token = Token
    numVIC = numVIC
    save_Cuenta(side, Token, NumATA)


def List():
    country_codes = {
    "Afganistán": "+93",
    "Albania": "+355",
    "Argelia": "+213",
    "Andorra": "+376",
    "Angola": "+244",
    "Antigua y Barbuda": "+1-268",
    "Argentina": "+54",
    "Armenia": "+374",
    "Australia": "+61",
    "Austria": "+43",
    "Azerbaiyán": "+994",
    "Bahamas": "+1-242",
    "Bahréin": "+973",
    "Bangladés": "+880",
    "Barbados": "+1-246",
    "Bielorrusia": "+375",
    "Bélgica": "+32",
    "Belice": "+501",
    "Benín": "+229",
    "Bután": "+975",
    "Bolivia": "+591",
    "Bosnia y Herzegovina": "+387",
    "Botsuana": "+267",
    "Brasil": "+55",
    "Brunéi": "+673",
    "Bulgaria": "+359",
    "Burkina Faso": "+226",
    "Burundi": "+257",
    "Cabo Verde": "+238",
    "Camboya": "+855",
    "Camerún": "+237",
    "Canadá": "+1",
    "República Centroafricana": "+236",
    "Chad": "+235",
    "Chile": "+56",
    "China": "+86",
    "Colombia": "+57",
    "Comoras": "+269",
    "Congo, República Democrática del": "+243",
    "Congo, República del": "+242",
    "Costa Rica": "+506",
    "Croacia": "+385",
    "Cuba": "+53",
    "Chipre": "+357",
    "Chequia": "+420",
    "Dinamarca": "+45",
    "Yibuti": "+253",
    "Dominica": "+1-767",
    "República Dominicana": "+1-809, +1-829, +1-849",
    "Timor Oriental": "+670",
    "Ecuador": "+593",
    "Egipto": "+20",
    "El Salvador": "+503",
    "Guinea Ecuatorial": "+240",
    "Eritrea": "+291",
    "Estonia": "+372",
    "Esuatini": "+268",
    "Etiopía": "+251",
    "Fiyi": "+679",
    "Finlandia": "+358",
    "Francia": "+33",
    "Gabón": "+241",
    "Gambia": "+220",
    "Georgia": "+995",
    "Alemania": "+49",
    "Ghana": "+233",
    "Grecia": "+30",
    "Granada": "+1-473",
    "Guatemala": "+502",
    "Guinea": "+224",
    "Guinea-Bisáu": "+245",
    "Guyana": "+592",
    "Haití": "+509",
    "Honduras": "+504",
    "Hungría": "+36",
    "Islandia": "+354",
    "India": "+91",
    "Indonesia": "+62",
    "Irán": "+98",
    "Irak": "+964",
    "Irlanda": "+353",
    "Israel": "+972",
    "Italia": "+39",
    "Costa de Marfil": "+225",
    "Jamaica": "+1-876",
    "Japón": "+81",
    "Jordania": "+962",
    "Kazajistán": "+7",
    "Kenia": "+254",
    "Kiribati": "+686",
    "Corea del Norte": "+850",
    "Corea del Sur": "+82",
    "Kuwait": "+965",
    "Kirguistán": "+996",
    "Laos": "+856",
    "Letonia": "+371",
    "Líbano": "+961",
    "Lesoto": "+266",
    "Liberia": "+231",
    "Libia": "+218",
    "Liechtenstein": "+423",
    "Lituania": "+370",
    "Luxemburgo": "+352",
    "Madagascar": "+261",
    "Malaui": "+265",
    "Malasia": "+60",
    "Maldivas": "+960",
    "Malí": "+223",
    "Malta": "+356",
    "Islas Marshall": "+692",
    "Mauritania": "+222",
    "Mauricio": "+230",
    "México": "+52",
    "Micronesia": "+691",
    "Moldavia": "+373",
    "Mónaco": "+377",
    "Mongolia": "+976",
    "Montenegro": "+382",
    "Marruecos": "+212",
    "Mozambique": "+258",
    "Birmania": "+95",
    "Namibia": "+264",
    "Nauru": "+674",
    "Nepal": "+977",
    "Países Bajos": "+31",
    "Nueva Zelanda": "+64",
    "Nicaragua": "+505",
    "Níger": "+227",
    "Nigeria": "+234",
    "Macedonia del Norte": "+389",
    "Noruega": "+47",
    "Omán": "+968",
    "Pakistán": "+92",
    "Palaos": "+680",
    "Panamá": "+507",
    "Papúa Nueva Guinea": "+675",
    "Paraguay": "+595",
    "Perú": "+51",
    "Filipinas": "+63",
    "Polonia": "+48",
    "Portugal": "+351",
    "Catar": "+974",
    "Rumania": "+40",
    "Rusia": "+7",
    "Ruanda": "+250",
    "San Cristóbal y Nieves": "+1-869",
    "Santa Lucía": "+1-758",
    "San Vicente y las Granadinas": "+1-784",
    "Samoa": "+685",
    "San Marino": "+378",
    "Santo Tomé y Príncipe": "+239",
    "Arabia Saudita": "+966",
    "Senegal": "+221",
    "Serbia": "+381",
    "Seychelles": "+248",
    "Sierra Leona": "+232",
    "Singapur": "+65",
    "Eslovaquia": "+421",
    "Eslovenia": "+386",
    "Islas Salomón": "+677",
    "Somalia": "+252",
    "Sudáfrica": "+27",
    "Sudán del Sur": "+211",
    "España": "+34",
    "Sri Lanka": "+94",
    "Sudán": "+249",
    "Surinam": "+597",
    "Suecia": "+46",
    "Suiza": "+41",
    "Siria": "+963",
    "Taiwán": "+886",
    "Tayikistán": "+992",
    "Tanzania": "+255",
    "Tailandia": "+66",
    "Togo": "+228",
    "Tonga": "+676",
    "Trinidad y Tobago": "+1-868",
    "Túnez": "+216",
    "Turquía": "+90",
    "Turkmenistán": "+993",
    "Tuvalu": "+688",
    "Uganda": "+256",
    "Ucrania": "+380",
    "Emiratos Árabes Unidos": "+971",
    "Reino Unido": "+44",
    "Estados Unidos": "+1",
    "Uruguay": "+598",
    "Uzbekistán": "+998",
    "Vanuatu": "+678",
    "Ciudad del Vaticano": "+379",
    "Venezuela": "+58",
    "Vietnam": "+84",
    "Yemen": "+967",
    "Zambia": "+260",
    "Zimbabue": "+263"}
    print("** Buscador de Codigos Internacionales **\n")
    def search_country_code(country):
        return country_codes.get(country, "País no encontrado")
    while True:
        country = input("\nIngrese el nombre del país (o '#' para Salir del Buscador): ")
        if country.lower() == '#':
            break
        code = search_country_code(country)
        print(f"\n-- El código internacional de {country} es: {code}")


clear()
print("*** Creador de Cuentas Locales SMS desde Twilio ***")
side = input("\nIngresa tu SID (Mostrada En Twilio): ")
Token = input("\nIngresa Tu Token (Mostrada En Twilio): ")
NumATA = int(input("\nIngresa Tu Numero de Telefono Twilio: \n"))

note = input("¿Los Datos Ingresados Son Correctos? (s/n): ")
while note == "n":
    side = input("\nIngresa Nuevamente tu SID (Mostrada En Twilio): ")
    Token = input("\nIngresa Nuevamente Tu Token (Mostrada En Twilio): ")
    NumATA = int(input("\nIngresa Nuevamente Tu Numero de Telefono Twilio: \n"))
    note = input("\n¿Los Datos Ingresados Son Correctos? (s/n): ")

clear()
print("Datos Ingresados:\n")
print(f"-- SID: {side}")
print(f"-- Token: {Token}")
print(f"-- Tu Numero: {NumATA}")
print("\nA Continuacion se realizara una prueba, con los datos Ingresados...")
print("\nIngresa Un Numero De Telefono para Recibir El Texto de Prueba (El Numero de Destino debe Contener el codigo Internacional)")
print("Si No conoces tu Numero Internacional, coloca un # ")
numVIC = input("Ingresa El Numero: ")
if numVIC == "#":
    clear()
    List()
    print("\nIngresa Un Numero De Telefono para Recibir El Texto de Prueba (El Numero de Destino debe Contener el codigo Internacional)")
    numVIC = input("Ingresa El Numero: ")
clear()
SubMain(side, Token, NumATA, numVIC)

