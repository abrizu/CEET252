def greet():
    print("Hello! My First Python Program")

def new_ln(input_str:str):
    for char in input_str:
        print(char + "\n", end="")

def main():
    greet()
    new_ln(("hello world").upper())

if __name__ == "__main__":
    main()