class U3A:
    def __init__(self, fahrenheit_input):
        self.fahrenheit_input = fahrenheit_input

    def conversion(self):
        celsius = (float(self.fahrenheit_input) - 32) * 5.0 / 9.0
        return round(celsius, 2)

def main():
    fahrenheit = input("Input a fahrenheit temperature: ")

    converter = U3A(fahrenheit)
    print(f"Converted Celsius is: {converter.conversion()}")

if __name__ == "__main__":
    main()



