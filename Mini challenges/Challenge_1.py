def imprmir_alrevez (palabra_usuario):
    
    if len(palabra_usuario)== 0:
        return""
    
    else:
        return palabra_usuario[-1] + imprmir_alrevez (palabra_usuario[:-1])
    
palabra = imprmir_alrevez (input("Ingresar palabra "))
print (palabra)