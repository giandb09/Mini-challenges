def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista = [60, 70, 40, 50, 30, 20, 10]

print("Lista original:")
print(lista)

ordenamiento_burbuja(lista)

print("Lista ordenada:")
print(lista)