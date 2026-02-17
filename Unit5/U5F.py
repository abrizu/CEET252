import math

class U5F:

    # THIS IS THE SAME CODE AS U4C
    # already handled each through individual methods, 
    # so no need to change anything for this unit
    
    @staticmethod
    def square(s:float = 0): # = 0; typehints float, otherwise default to 0
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
            area = U5F.square(s)
            print(f"Area of square: {area:.2f}")
            cond = True

        elif option == 2:
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = U5F.rectangle(l, w)
            print(f"Area of rectangle: {area:.2f}")
            cond = True

        elif option == 3:
            r = float(input("Enter radius: "))
            area = U5F.circle(r)
            print(f"Area of circle: {area:.2f}")
            cond = True

        else:
            print("Invalid option. \n")

if __name__ == "__main__":
    main()

    