import random
#same as the other, but its on a different.py to show how i have changed it
#this one makes use of my c1 recursion factorial finder

def factorialfinder(integer):
    if (integer>0):
        return integer * factorialfinder(integer-1) 
    elif integer == 0:
        return 1
    
digit1 = int(input("input digit1 "))
digit2 = int(input("input digit2 "))
digit3 = int(input("input digit3 "))
digit4 = int(input("input digit4 "))
count = 0
numOfLists = 0
combinations = []

listofnumbers = [digit1, digit2, digit3, digit4]
numberstouse = []
samedigit = 1
for i in range(len(listofnumbers)):
    if listofnumbers[i] in numberstouse:
        samedigit = samedigit+1
    numberstouse.append(listofnumbers[i])
possibledigits = 4 - samedigit
possiblecombinations = factorialfinder(len(numberstouse)) / factorialfinder(len(numberstouse)-possibledigits)

while numOfLists < possiblecombinations:
    newlist = ""
    numberstouse = [digit1, digit2, digit3, digit4]
    
    for i in range(4):
        indextoadd = random.randint(0,len(numberstouse)-1)
        newlist = newlist + str(numberstouse[indextoadd])
        del numberstouse[indextoadd]

    if newlist not in combinations:
        combinations.append(newlist)
        count = 0
        numOfLists = numOfLists + 1
    else:
        count = count + 1
print(combinations)
print(numOfLists, "combinations")