#include <iostream>
#include <cmath>

int calculations(float w, float h, float l, float p, float e) {

    float I, D, B;

    // calculations
    I = w * std::pow(h, 3) / 12.0f;
    D = p * std::pow(l, 3) / (3 * e * I);
    B = p * l * h / (2 * I);

    // rounding
    I = std::round(I * 100.0f) / 100.0f;
    D = std::round(D * 100.0f) / 100.0f;
    B = std::round(B * 100.0f) / 100.0f;

    // output
    std::cout << "\nMoment of Inertia (I) = " << I << std::endl;
    std::cout << "Deflection (D) = " << D << std::endl;
    std::cout << "Bending Stress (B) = " << B << std::endl;

    return 0;
}

int main() {

    float w, h, l, p, e;

    std::cout << "Enter width of the beam (W): ";
    std::cin >> w;

    std::cout << "Enter height of the beam (H): ";
    std::cin >> h;

    std::cout << "Enter length of the beam (L): ";
    std::cin >> l;

    std::cout << "Enter force applied (P): ";
    std::cin >> p;

    std::cout << "Enter Modulus of Elasticity (E): ";
    std::cin >> e;

    calculations(w, h, l, p, e);

}