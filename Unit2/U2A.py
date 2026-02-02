# forewarning: cs student, primary coding language is python.
# some code i produce may be out of the scope
# of what we learned in this class. all of my code is original, and
# learned on my own.

# stuff most likely not covered --
# @staticmethod: method decorator to convert function into static
# static function?: utility functions within a class that do not need 'self' arg

# def example(x:float = 100.0):
# x:float -> type hinting. method always should expect a float for x.
# = 100 -> defaults to 100.0.

# 
def print_output():
    print((5*"Yes"))
    print((3*"Maybe")+(5*"Yes"))
    print((3*"I don't know! "))

def main(): # always follow proper python conventions
    print_output()

if __name__ == "__main__":
    main()

