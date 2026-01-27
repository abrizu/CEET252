class U1A:
    def __init__(self, name="", contact=""): # initializes name and contact variables, default to empty str
        self.name = name
        self.contact = contact

    def introduction(self, name, contact):
        print(f"Hello, my name is {name}. You can contact me at {contact}.")

    def triangle(self):
        print("This is my triangle")
        print("  /\\  \n /  \\ \n/____\\")
        # backslashes require escaping -> \\
        # \n allows us to go to the next line

def main(): # main function used to run program. supports basic OOP
    name = "Aaron Brizuela"
    contact = "734-xxx-xxxx"

    U1A().introduction(name, contact)
    U1A().triangle()

if __name__ == "__main__":
    main()