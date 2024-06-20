import random
import string

def generar_contrasena(longitud):
    # Definir los caracteres permitidos
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Combinar todos los caracteres permitidos
    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos

    # Verificar que la longitud esté en el rango permitido
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud de la contraseña debe estar entre 8 y 16 caracteres")

    # Generar la contraseña asegurando que contenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completar la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
    contrasena += random.choices(todos_caracteres, k=longitud - len(contrasena))

    # Mezclar los caracteres para evitar cualquier patrón
    random.shuffle(contrasena)

    # Convertir la lista a una cadena
    contrasena = ''.join(contrasena)
    
    return contrasena

# Solicitar la longitud de la contraseña al usuario
longitud = int(input("Ingresa la longitud deseada para la contraseña (entre 8 y 16 caracteres): "))

# Generar la contraseña
contrasena_segura = generar_contrasena(longitud)

# Imprimir la contraseña generada
print("Contraseña segura generada:", contrasena_segura)
