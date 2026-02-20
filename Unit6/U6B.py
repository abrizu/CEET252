import csv

class U6B:

    def read_csv(self):
        names = []

        try:
            with open("U6B-CSV.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(row) # print structure of scv
                    if row:
                        names.append(row[1]) # print only names (index 1)

            file.close()

        except Exception as e:
            print(f"An error occurred: {e}")

        return names
    
def main():
    csv_handler = U6B()
    names = csv_handler.read_csv()
    print("------------------")
    for name in names:
        print(name)

if __name__ == "__main__":
    main()