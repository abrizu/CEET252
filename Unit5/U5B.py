class U5B:
    def __init__(self, username:str, amount:float, due_date:str): 
        # passed to the init function, 
        # and uses self to assign the values to the class attributes.
 
        self.username = username
        self.amount = amount
        self.due_date = due_date

    def display_invoice(self):
        print(f"Hello {self.username}\nYour bill of ${self.amount:.2f} is due on {self.due_date}.")

def main():
    invoice = U5B("Joseph", 150.36, "12/30/2025")
    invoice.display_invoice()

    invoice = U5B("Joy", 50.00, "12/15/2025") 
    invoice.display_invoice()

if __name__ == "__main__":
    main()