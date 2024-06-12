def multiplicacion():
    numero_ingresado_usuario = int(input("Ingrese un numero"))
    for i in range (0,11):
        numero_multiplicador = numero_ingresado_usuario*i
        
        print (numero_multiplicador)
        
multiplicacion()