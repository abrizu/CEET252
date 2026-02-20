class U6C:

    @staticmethod
    def multiplication_table(r, c):

        # nested for loops for 2d table
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                print(f"{i * j:4}", end="\t")
            print() # new line after each row 

def main():
    row = int(input("Row number: "))
    col = int(input("Column number: "))

    U6C.multiplication_table(row, col)

if __name__ == "__main__":
    main()
