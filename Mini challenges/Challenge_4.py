# Función para ordenar una lista de números en orden ascendente
def ordenar_lista(lista):
    # Utilizamos la función sorted para ordenar la lista
    lista_ordenada = sorted(lista)
    return lista_ordenada

# Pedir al usuario que ingrese la lista de números
entrada = input("Ingresa una lista de números separadas por espacios: ")

# Convertir la entrada en una lista de números
numeros = [int(numero) for numero in entrada.split()]

# Llamar a la función para ordenar la lista
lista_ordenada = ordenar_lista(numeros)

# Imprimir la lista ordenada
print("Lista ordenada en orden ascendente:", lista_ordenada)