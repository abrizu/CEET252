def introductions(first_name:str, color:str):
    print(f"{first_name.title()} likes {color.lower()}.")

def main():
    first_name = str(input(f"What is your first name? "))
    color = str(input(f"What is your favorite color? "))
    introductions(first_name, color)

if __name__ == "__main__":
    main()
