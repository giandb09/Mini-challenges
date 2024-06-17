def crear_diccionario(claves, valores):
    # Verificamos que las listas tengan la misma longitud
    if len(claves) != len(valores):
        raise ValueError("Las listas de claves y valores deben tener la misma longitud")
    
    # Creamos el diccionario utilizando zip
    diccionario = dict(zip(claves, valores))
    return diccionario

# Ejemplo de uso:
claves = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Llamamos a la función para crear el diccionario
diccionario_resultante = crear_diccionario(claves, valores)

# Imprimimos el diccionario resultante
print("Diccionario resultante:", diccionario_resultante)