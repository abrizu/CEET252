#include <iostream>
#include <cmath>

int algorithm(float x, float y) {

    float t;

    // check zeros
    if (x == 0 || y == 0) {
        std::cout << "One of x or y is zero!" << std::endl;
        return 0;
    }

    // operations
    if (x > 0 && y > 0) {
        t = x + y;
        std::cout << "t = x + y = ";
    } else if (x > 0 && y < 0) {
        t = x - y;
        std::cout << "t = x - y = ";
    } else if (x < 0 && y < 0) {
        t = x * y;
        std::cout << "t = x * y = ";
    } else if (x < 0 && y > 0) {
        t = x / y;
        std::cout << "t = x / y = ";
    }

    // round to 2 decimal places
    t = std::round(t * 100.0f) / 100.0f;
    std::cout << t << std::endl;

    return 0;
}

int main() {
    float x, y;

    std::cout << "Please enter a float number for x: ";
    std::cin >> x;

    std::cout << "Please enter a float number for y: ";
    std::cin >> y;

    algorithm(x, y);
}