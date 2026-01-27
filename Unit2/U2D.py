def main(): # got lazy for oop so just put it in main
    num_list = []

    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    num_list.append(num1)
    num_list.append(num2)

    print(f"The sum of {num1} and {num2} is {sum(num_list)}")
    print(f"The average of ({num1} + {num2}) is {round(sum(num_list)/len(num_list), 1)}")

if __name__ == "__main__":
    main()