def greet():
    print("Hello! My First Python Program")

def new_ln(input_str:str): # type hinting: expects a str as input
    for char in input_str:
        print(char + "\n", end="") # ends print stmt inline. good for concatenation

def main():
    greet()
    new_ln(("hello world").upper())

if __name__ == "__main__":
    main()