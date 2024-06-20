import random

def obtener_eleccion_computadora():
    # Generar una elección aleatoria para la computadora
    opciones = ["piedra", "papel", "tijeras"]
    eleccion = random.choice(opciones)
    return eleccion

def determinar_ganador(usuario, computadora):
    # Determinar el ganador del juego
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "Usuario"
    else:
        return "Computadora"

def jugar_piedra_papel_tijeras():
    # Solicitar la elección del usuario
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    
    # Validar la elección del usuario
    if usuario not in ["piedra", "papel", "tijeras"]:
        print("Elección inválida, por favor elige piedra, papel o tijeras.")
        return
    
    # Obtener la elección de la computadora
    computadora = obtener_eleccion_computadora()
    print(f"Computadora eligió: {computadora}")
    
    # Determinar el ganador
    ganador = determinar_ganador(usuario, computadora)
    
    # Mostrar el resultado
    if ganador == "Empate":
        print("Es un empate.")
    elif ganador == "Usuario":
        print("¡Ganaste!")
    else:
        print("La computadora gana.")

# Ejecutar el juego
jugar_piedra_papel_tijeras()