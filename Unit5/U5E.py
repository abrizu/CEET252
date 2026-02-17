import math

class U5E:

    @staticmethod
    def eqn(x):
        y = x * math.exp(-x) + math.sqrt(1 - math.exp(-x))
        return y

def main():
    for x in [5, 6.5, 7, 8.9]: # hard coded x values
        print(f"at x = {x:.4f}, y = {U5E.eqn(x):.4f}")

if __name__ == "__main__":
    main()

