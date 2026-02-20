import math

class U5G:

    @staticmethod
    def roots(a, b, c):
        discriminant = (b**2) - (4*a*c)

        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)

            print(f"x1: {root1:.4f}")
            print(f"x2: {root2:.4f}")

        else:
            print("Neither solutions are real numbers.")

def main():
    cond = False

    while cond != True:
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))

        if a == 0:
            print("'a' can't be 0!")

        else:
            print(f"a, b, c: {a}, {b}, {c}")
            U5G.roots(a, b, c)

        cond = True

if __name__ == "__main__":
    main()