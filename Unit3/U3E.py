class U3E:
    def __init__(self, test_one, test_two, final, assignments):
        self.test_one = test_one
        self.test_two = test_two
        self.final = final
        self.assignments = assignments

    def calculate_grade(self):
        total_grade = self.test_one + self.test_two + self.final + self.assignments
        return round(total_grade, 2)

    def assign_letter(self, grade):
        grade_chart = [ 
            # did not want to if-elif chain grades. 
            # instead use list of tuples (immutable) 
            # to store the min grade of each letter value

            (95, 'A'), (90, 'A-'),
            (87, 'B+'), (84, 'B'), (80, 'B-'),
            (77, 'C+'), (74, 'C'), (70, 'C-'),
            (67, 'D+'), (64, 'D'), (60, 'D-')
        ]

        for min_grade, letter in grade_chart:
            if grade >= min_grade:
                return letter
            
        # anything else fails
        return 'F'

def main():
    t1 = float(input("Enter the grade of the first test (0-15): "))
    t2 = float(input("Enter the grade of the second test (0-15): "))
    fin = float(input("Enter the grade of the final exam (0-20): "))
    assign = float(input("Enter the total grade of the assignments (0-50): "))

    student_grade = U3E(t1, t2, fin, assign)
    numeric_grade = student_grade.calculate_grade()
    letter_grade = student_grade.assign_letter(numeric_grade)

    print(f"The final grade calculated is {numeric_grade}")
    print(f"Your grade is \"{letter_grade}\"")
    

if __name__ == "__main__":
    main()
