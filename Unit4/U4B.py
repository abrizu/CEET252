import math

class U4B:

    @staticmethod
    def equation(x:float):
        return x * math.exp(-x) + math.sqrt((1 - math.exp(-x)))
    
    @staticmethod
    def equation(x_start:float, x_end:float, div_num:float):
        for i in range(x_start, x_end, div_num):
            return x * math.exp(-x) + math.sqrt((1 - math.exp(-x)))

def main():

    x_start = float(input("x_start "))
    x_end = float(input("x_end: "))
    div_num = float(input("div_num: "))

    res7 = U4B.equation(x_start, x_start, x_end, div_num)

    print("\n=== Equation 7 Result ===")
    print(f"EQ7: {res7:.4f}")
    print("=========================")

if __name__ == "__main__":
    main()