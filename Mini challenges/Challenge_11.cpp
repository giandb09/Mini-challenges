#include <iostream>
#include <string>
#include <algorithm>

bool esPalindromo(const std::string &str) {

    std::string str_sin_espacios;
    std::remove_copy_if(str.begin(), str.end(), std::back_inserter(str_sin_espacios), ispunct);
    std::transform(str_sin_espacios.begin(), str_sin_espacios.end(), str_sin_espacios.begin(), ::tolower);
    
    std::string reversa = str_sin_espacios;
    std::reverse(reversa.begin(), reversa.end());
    
    return str_sin_espacios == reversa;
}

int main() {
    std::string cadena;
    
    std::cout << "Ingrese una palabra para verificar si es un palíndromo: ";
    std::getline(std::cin, cadena);
    
    if (esPalindromo(cadena)) {
        std::cout << "La palabra ingresada es un palíndromo." << std::endl;
    } else {
        std::cout << "La palabra ingresada no es un palíndromo." << std::endl;
    }
    
    return 0;
}
