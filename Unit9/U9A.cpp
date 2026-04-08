#include <iostream>
#include <cmath>

float FahrenheitToCelsius(float fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

int main() {
    float fahrenheit;
    std::cout << "Enter temperature in fahrenheit: ";
    std::cin >> fahrenheit;

    float celsius = FahrenheitToCelsius(fahrenheit);
    celsius = std::round(celsius * 100.0) / 100.0;
    std::cout << "Temperature in Celsius: " << celsius << std::endl;

    return 0;
}