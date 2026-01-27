class U3C:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def assign(self):
        if self.x > 0 and self.y > 0: # both pos
            print("t = x+y = ", end='')
            self.t = self.x + self.y

        elif self.x > 0 and self.y < 0: # x pos, y neg
            print("t = x-y = ", end='')
            self.t = self.x - self.y

        elif self.x < 0 and self.y < 0: # both neg
            print("t = x*y = ", end='')
            self.t = self.x * self.y

        elif self.x < 0 and self.y > 0: # x neg, y pos
            print("t = x/y = ", end='')
            self.t = self.x / self.y
        
        else:
            print("One of x or y is zero!")
            exit() # break out of program if zero

        return print(f"{round(self.t, 2)}\n")
        
def main():
    x = float(input("Enter value for x: "))
    y = float(input("Enter value for y: "))
    t = U3C(x, y, 0)
    t.assign()

if __name__ == "__main__":
    main()
