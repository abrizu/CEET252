class U5A:
    def __init__(self, name:str, age:int):
        # name and age are passed to the init function,
        # and uses self to assign the values to the class attributes.

        self.name = name
        self.age = age

    def happy_birthday(self):
        print(f"Happy Birthday to {self.name}!\nYou are {self.age} years old!")
        print("Happy birthday to you!\n")

def main():

    birthday = U5A("Joseph", 22) # create a class instance with name and age
    birthday.happy_birthday()

    birthday = U5A("Myself", 45) # overwritten class instance
    birthday.happy_birthday()

if __name__ == "__main__":
    main()