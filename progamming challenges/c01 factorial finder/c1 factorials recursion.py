def factorialfinder(integer):
    if (integer>0):
        return integer * factorialfinder(integer-1) 
    elif integer == 0:
        return 1
integer = int(input("input a number to find the factorial of"))
print(factorialfinder(integer))