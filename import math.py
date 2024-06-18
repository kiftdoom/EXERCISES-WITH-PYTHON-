import math

def calculate_square_root(Result):
    if Result < 0:
        return "You cannot calculate the square root of a negative number."
    else:
        return math.sqrt(Result)
        
number = float(input("Enter a number: "))
Result = calculate_square_root(number)
print("Result:", Result)
