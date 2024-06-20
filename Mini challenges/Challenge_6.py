def celsius_a_fahrenheit(celsius):
    # Fórmula de conversión de Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Pedir al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Llamar a la función para convertir la temperatura a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Imprimir la temperatura convertida
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")