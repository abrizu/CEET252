class U5D:
    def __init__(self, name:str = "Aaron", state:str = "Virginia"):
        self.name = name
        self.state = state

    def name_born(self):
        print(f"{self.name} was born in {self.state}.")

def main():
    dad = U5D("Dad", "Chicago")
    mom = U5D("Mom", "California")
    myself = U5D() # default values

    dad.name_born()
    mom.name_born()
    myself.name_born()

if __name__ == "__main__":
    main()
