#include <iostream>
#include <cmath>

char gradesCalculator(float score) {
    if (score >= 90.0) return 'A';
    else if (score >= 80.0) return 'B';
    else if (score >= 70.0) return 'C';
    else if (score >= 60.0) return 'D';
    else return 'F';
}

int main() {
    std::cout << "Calculating the final grade and assign a letter grade\n";

    float first, second, finalExam, assignments;

    std::cout << "Enter the grade of the first test (0-15): ";
    std::cin >> first;
    std::cout << "Enter the grade of the second test (0-15): ";
    std::cin >> second;
    std::cout << "Enter the grade of the final exam (0-20): ";
    std::cin >> finalExam;
    std::cout << "Enter the total grade of the assignments (0-50): ";
    std::cin >> assignments;

    // Input validation
    if (first < 0.0 || first > 15.0 || second < 0.0 || second > 15.0 ||
        finalExam < 0.0 || finalExam > 20.0 || assignments < 0.0 || assignments > 50.0) {
        std::cout << "Invalid input! Please enter values in the correct range." << std::endl;
        return 1;
    }

    float score = first + second + finalExam + assignments;
    std::cout << "The final grade calculated is: " << score << std::endl;

    int roundedScore = static_cast<int>(std::round(score)); // cast it to an int, round to 2 decimals up
    std::cout << "The rounded grade is: " << roundedScore << std::endl;

    char grade = gradesCalculator(score);
    std::cout << "Your grade is: " << grade << std::endl;

    return 0;
}