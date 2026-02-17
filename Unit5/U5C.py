class U5C:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        try:
            return self.x / self.y
        except ZeroDivisionError: # try-catch to catch any div by zero errors
            return "Cannot divide by zero!"
        
def main():
    # ADDED: a simple calculator UI to dynamically test methods of the class
    # makes it more interactive for multiple calculations

    print("=== Calculator ===")

    while True: # constantly loop until break
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5": # early break
            print("Exiting the calculator.")
            break

        if choice not in {"1", "2", "3", "4"}: # invalid catch operation
            print("Invalid choice. Please select a valid operation.")
            continue

        x = float(input("Enter value for x: "))
        y = float(input("Enter value for y: "))
        calculator = U5C(x, y) # assign class to x, y values and pull using self

        match choice: # love using match-case for cleaner code than repetitive if-else statements
            case "1":
                print(f"Result: {calculator.add()}")
            case "2":
                print(f"Result: {calculator.subtract()}")
            case "3":
                print(f"Result: {calculator.multiply()}")
            case "4":
                print(f"Result: {calculator.divide():.2f}")

if __name__ == "__main__":
    main()