def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False

# Lista ordenada de 10 elementos
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Solicitar al usuario que ingrese el número a buscar
numero_a_buscar = int(input("Ingresa el numero que deseas buscar en la lista: "))

# Llamar a la función de búsqueda binaria
encontrado = busqueda_binaria(lista_ordenada, numero_a_buscar)

# Imprimir el resultado
if encontrado:
    print(f"El numero {numero_a_buscar} se encuentra en la lista.")
else:
    print(f"El numero {numero_a_buscar} no se encuentra en la lista.")
