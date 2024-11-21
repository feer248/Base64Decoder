#!/usr/bin/python3

import base64
import sys

def decode_base64_repeatedly(input_file):
    try:
        # Lee el contenido del archivo
        with open(input_file, 'r') as file:
            encoded_data = file.read().strip()
        
        # Decodifica repetidamente hasta que ya no sea base64
        while True:
            try:
                # Intenta decodificar la cadena
                decoded_data = base64.b64decode(encoded_data).decode('utf-8')
                encoded_data = decoded_data
            except (base64.binascii.Error, UnicodeDecodeError):
                # Si falla, se asume que ya no es Base64
                break

        # Pregunta al usuario si desea guardar o mostrar el resultado
        user_choice = input("¿Deseas guardar el resultado en un archivo? (s/n): ").strip().lower()
        
        if user_choice == 's':
            output_file = input("Ingresa el nombre del archivo de salida (ej. resultado.txt): ").strip()
            with open(output_file, 'w') as file:
                file.write(decoded_data)
            print(f"Decodificación completada. El resultado se ha guardado en {output_file}")
        else:
            print("\nResultado de la decodificación:")
            print(decoded_data)
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Verifica que el archivo de entrada se haya proporcionado como argumento
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <archivo_codificado.txt>")
    else:
        input_file = sys.argv[1]
        decode_base64_repeatedly(input_file)
