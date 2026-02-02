class mathing:
    def __init__(self, num_list):
        self.num_list = num_list

    def max(self):
        # for i in self.num_list:
        #     if i == max(self.num_list):
        #         # just using the basic max() function for simplicity
        #         # what max / min does: loop through list, if next num is max / min, assign it as i else skip
        #         return i
            
            # simplified version: (python is cool like that)
            return max(self.num_list)
            

    def min(self):
        # for i in self.num_list:
        #     if i == min(self.num_list):
        #         # same for min()
        #         return i
            
            # simplified version:
            return min(self.num_list)
    
    def avg(self): # all num divided by count len
        return round(sum(self.num_list) / len(self.num_list), 1) # round to first decimal
    
def main():
    num_list = []
    suffixes = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th'} # dictionary of suffixes
    # do not need math formula for suffixes; only 4 inputs

    for x in range(4): # loop for 4 floats
        suffix = suffixes[x + 1]
        index = float(input(f"Enter {x+1}{suffix} number: "))
        num_list.append(index)

    print(f"\nnum_list: {num_list}\n") # debug

    print("=== MATH FUNCTIONS ===")
    print(f"The max value is: {mathing(num_list).max()}")
    print(f"The min value is: {mathing(num_list).min()}")
    print(f"The average is: {mathing(num_list).avg()}")

if __name__ == "__main__":
    main()
