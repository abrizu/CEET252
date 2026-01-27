class U3B:
    def __init__(self, credits):
        self.credits = credits

    def graduation_req(self):
        if self.credits >= 120: # emu now requires 120 credits to graduate, not 124
            return "You have enough credits to graduate!"
        else:
            return f"You don't have enough credits. You need {120 - self.credits} more credits to graduate."

def main():
    credits = int(input("Enter the number of credits you have earned: "))

    student = U3B(credits)
    print(student.graduation_req())

if __name__ == "__main__":
    main()