def factorialfinder(integer):
    if (integer>0):
        total = integer * factorialfinder(integer-1) 
    return total
integer = int(input("input a number to find the factorial of"))
print(factorialfinder(integer))