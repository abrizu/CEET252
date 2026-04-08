#include <iostream>

int creditsForGraduation(int credits) {
    if (credits >= 124) {
        return 0; // no more credits needed to graduate
    } else {
        return 124 - credits; // credits needed to graduate
    }
}

int main() {
    int credits;
    std::cout << "Input credit hours earned at EMU: ";
    std::cin >> credits;

    int creditsNeeded = creditsForGraduation(credits);
    if (creditsNeeded == 0) {
        std::cout << "You have enough credits - Congratulations!" << std::endl;
    } else {
        std::cout << "You need " << creditsNeeded << " more credit hours to graduate." << std::endl;
    }
}