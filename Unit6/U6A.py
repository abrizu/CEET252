class U6A:
    def open_file(self):
        try:
            with open("U6A.txt", "w") as file:
                file.write("Happy birthday to mom!\nYou are 44 years old!\nWish you stay young forever!")
            file.close()
        except Exception as e:
            print(f"An error occurred: {e}")

    def read_file(self):
        try:
            with open("U6A.txt", "r") as file:
                content = file.read()
                print(content)
            file.close()
        except Exception as e:  
            print(f"An error occurred: {e}")

def main():
    file_handler = U6A()
    file_handler.open_file()
    file_handler.read_file()

if __name__ == "__main__":
    main()


