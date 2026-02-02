import math

class U4B:
    
    @staticmethod # helper method to run the equation per each y input
    def equation(x:float): # x:float ensures that the input is treated as float (even though input explicitly converts to float)
        return x * math.exp(-x) + math.sqrt((1 - math.exp(-x)))

    @staticmethod
    def y(x_start:float, x_end:float, div_num:int): # iterates points per step
        step = (x_end - x_start) / div_num
        for i in range(div_num + 1):
            x = x_start + i * step
            y = U4B.equation(x)
            print(f"Point {i+1} at x: {x:.4f}, y: {y:.4f}")
        
def main():

    x_start = float(input("Enter a starting value for the equation: "))
    x_end = float(input("Enter an ending value for the equation: "))
    div_num = int(input("Enter the division number (positive integer): "))

    print("---------------------------------")
    print("You enter 4 divisions, and 5 data points will be calculated.")
    U4B.y(x_start, x_end, div_num)
    print()

if __name__ == "__main__":
    main()