import math

class U4C:
    
    @staticmethod
    def square(s:float = 0):
        return s**2

    @staticmethod
    def rectangle(l:float = 0, w:float = 0):
        return l * w

    @staticmethod
    def circle(r:float = 0):
        return math.pi * r * r

def main():
    print("Choose an option to calculate area:")
    print("1) Square")
    print("2) Rectangle")
    print("3) Circle")

    cond = False # flag to repeat option if wrong option

    while (cond is not True):
        option = int(input("Enter your option (1, 2, or 3): "))

        if option == 1:
            s = float(input("Enter side length: "))
            area = U4C.square(s)
            print(f"Area of square: {area:.4f}")
            cond = True

        elif option == 2:
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = U4C.rectangle(l, w)
            print(f"Area of rectangle: {area:.4f}")
            cond = True

        elif option == 3:
            r = float(input("Enter radius: "))
            area = U4C.circle(r)
            print(f"Area of circle: {area:.4f}")
            cond = True

        else:
            print("Invalid option. \n")

if __name__ == "__main__":
    main()

    