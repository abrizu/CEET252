import math

class U4D:

    @staticmethod
    def quadratic(a, b, c):
        discriminant = b**2 - 4*a*c

        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)

            print(f"Root 1: {root1:.4f}")
            print(f"Root 2: {root2:.4f}")

        else:
            print("Neither solutions are real numbers.")

def main():

    cond = False

    while cond != True:
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))

        if a == 0:
            print("a cannot be 0")

        U4D.quadratic(a, b, c)
        cond = True

if __name__ == "__main__":
    main()