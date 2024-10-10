import random

def factorialfinder(integer):
    if (integer>0):
        return integer * factorialfinder(integer-1) 
    elif integer == 0:
        return 1



def genpocketchange():

    changeinpocket = []
    for i in range(len(incirculation)):
        number = random.randint(0, int((120/incirculation[i])-1))
        for y in range(number):
            changeinpocket.append(incirculation[i])
    print(changeinpocket)
    return changeinpocket

incirculation = [1,2,3,4,5,6,10,12,15,20,30,60]

listofnumbers = genpocketchange()
numberstouse = []
uniquedigits = 0
for i in range(len(listofnumbers)):
    if listofnumbers[i] not in numberstouse:
        uniquedigits +=1
    numberstouse.append(listofnumbers[i])
uniquedigits -=1
possiblecombinations = factorialfinder(len(numberstouse)) /a/ (factorialfinder(uniquedigits) * factorialfinder(len(numberstouse)-uniquedigits))
print(uniquedigits)
print(possiblecombinations)

numOfLists = 0
combinations = []

while numOfLists < possiblecombinations:
    newlist = ""
    changetotest = numberstouse
    
    for i in range(len(numberstouse)):
        indextoadd = random.randint(0,len(changetotest)-1)
        newlist = newlist + str(changetotest[indextoadd])
        del changetotest[indextoadd]
    
    if newlist not in combinations:
        combinations.append(newlist)
        numOfLists = numOfLists + 1
print(combinations)
print(numOfLists, "combinations")