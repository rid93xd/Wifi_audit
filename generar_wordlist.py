# Lista para almacenar palabras con 8 o más caracteres
palabras_largas = []

# Solicita al usuario la dirección del archivo
archivo = input("Por favor, introduce la ruta del archivo que contiene la lista de palabras: ")

try:
    # Abre el archivo en modo lectura, especificando 'latin-1' como el encoding
    with open(archivo, 'r', encoding='latin-1') as f:
        # Lee cada línea del archivo
        for linea in f:
            # Elimina los espacios en blanco al principio y al final de la línea
            palabra = linea.strip()
            # Verifica si la palabra tiene 8 o más caracteres y la agrega a la lista palabras_largas
            if len(palabra) >= 8:
                palabras_largas.append(palabra)

    # Define la ruta del archivo de salida
    archivo_salida = "palabras_largas.txt"
    
    # Abre el archivo de salida en modo escritura
    with open(archivo_salida, 'w') as f:
        # Escribe cada palabra en una línea del archivo de salida
        for palabra in palabras_largas:
            f.write(palabra + '\n')

    print(f"Se han guardado las palabras con 8 o más caracteres en el archivo {archivo_salida}.")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta proporcionada.")
except Exception as e:
    print("Ocurrió un error:", e)
