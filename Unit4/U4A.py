import math

class U4A:

    # since these are utility functions, we can use static methods to clean it up

    @staticmethod
    def equation_1(x):
        return (x - 5/2) ** 6 - (17/4)
    
    @staticmethod
    def equation_2(x):
        return math.sin(2*x) * math.cos(3*x) + math.sin(4*x)**4
    
    @staticmethod
    def equation_3(x, n):
        return 1 + (n*x)/math.factorial(4) + n*(n-1)*(x**2)/math.factorial(8)

    @staticmethod
    def equation_4(x):
        return math.exp(x**2) * math.log(26)
    
    @staticmethod
    def equation_5(x):
        return math.log10(x) - math.sin(3*x)
    
    @staticmethod
    def equation_6(x):
        return math.log(math.exp(x))


def main():
    x = float(input("Enter a value for x: "))
    n = float(input("Enter a value for n: "))

    res1 = U4A.equation_1(x)
    res2 = U4A.equation_2(x)
    res3 = U4A.equation_3(x, n)
    res4 = U4A.equation_4(x)
    res5 = U4A.equation_5(x)
    res6 = U4A.equation_6(x)

    print("\n=== Equation Results ===")
    print(f"EQ1: {res1:.4f}")
    print(f"EQ2: {res2:.4f}")
    print(f"EQ3: {res3:.4f}")
    print(f"EQ4: {res4:.4f}")
    print(f"EQ5: {res5:.4f}")
    print(f"EQ6: {res6:.4f}")
    print("========================")

if __name__ == "__main__":
    main()

