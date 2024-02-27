# Solicita al usuario la dirección del archivo
archivo = input("Por favor, introduce la ruta del archivo que contiene la lista de palabras: ")

try:
    
    archivo_salida = "palabras_largas.txt"

    
    with open(archivo_salida, 'w') as f_salida:
       
        with open(archivo, 'r', encoding='latin-1') as f_entrada:
            
            for linea in f_entrada:
               
                palabra = linea.strip()
                
                if len(palabra) >= 8:
                    f_salida.write(palabra + '\n')

    print(f"Se han guardado las palabras con 8 o más caracteres en el archivo {archivo_salida}.")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta proporcionada.")
except Exception as e:
    print("Ocurrió un error:", e)
