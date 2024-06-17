def contar_vocales(cadena):
    # Convertimos la cadena a minúsculas para simplificar la comparación
    cadena = cadena.lower()
    
    # Definimos las vocales en una lista
    vocales = "aeiou"
    
    # Inicializamos un contador para las vocales
    contador = 0
    
    # Iteramos sobre cada caracter en la cadena
    for caracter in cadena:
        # Si el caracter es una vocal, incrementamos el contador
        if caracter in vocales:
            contador += 1
    
    # Devolvemos el contador que representa el número de vocales
    return contador

# Ejemplo de uso:
cadena = "Hola soy Gianfranco"
numero_vocales = contar_vocales(cadena)
print(f"El número de vocales en la cadena '{cadena}' es: {numero_vocales}")
