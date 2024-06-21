#include <iostream>

int main() {
    // Declarar variables para los dos números
    double num1, num2;

    // Pedir al usuario que ingrese el primer número
    std::cout << "Ingresa el primer número: ";
    std::cin >> num1;

    // Pedir al usuario que ingrese el segundo número
    std::cout << "Ingresa el segundo número: ";
    std::cin >> num2;

    // Sumar los dos números
    double suma = num1 + num2;

    // Imprimir la suma
    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << std::endl;

    return 0;
}