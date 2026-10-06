import string
from langdetect import detect, DetectorFactory

#pip install langdetect 

# Hacemos que la detección de idioma sea siempre reproducible
DetectorFactory.seed = 0

ALFABETO = string.ascii_lowercase


def descifrar_cesar(mensaje, clave):
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            letra = caracter.lower()

            posicion = ALFABETO.index(letra)
            nueva_posicion = (posicion - clave) % 26
            nueva_letra = ALFABETO[nueva_posicion]

            if mayuscula:
                nueva_letra = nueva_letra.upper()

            resultado += nueva_letra

        else:
            resultado += caracter

    return resultado


def ataque_fuerza_bruta(mensaje, idioma):
    for clave in range(26):
        texto = descifrar_cesar(mensaje, clave)

        try:
            idioma_detectado = detect(texto)

            if idioma_detectado == idioma:
                return clave, texto

        except:
            pass

    return None, None


# Programa principal

mensaje = input("Introduce el mensaje cifrado: ")

clave, mensaje_descifrado = ataque_fuerza_bruta(mensaje, "es")

if clave is not None:
    print("\n=== RESULTADO ===")
    print("Clave encontrada:", clave)
    print("Mensaje descifrado:", mensaje_descifrado)
else:
    print("\nNo se ha encontrado ninguna clave.")
