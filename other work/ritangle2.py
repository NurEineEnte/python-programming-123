import itertools
import random

incirculation = [1,2,3,4,5,6,10,12,15,20,30,60]

def genpocketchange():

    changeinpocket = []
    for i in range(len(incirculation)):
        number = random.randint(0, int((120/incirculation[i])-1))
        for y in range(number):
            changeinpocket.append(incirculation[i])
    print(changeinpocket)
    return changeinpocket


def sumlist(list):
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    return total
         
def explorethischange(change):
    highestvalue = 0
    for i in range(len(change), 0, -1):
        for seq in itertools.combinations(change, i):
            if sumlist(seq) == 120:
                print("found")
                return 0

        print(highestvalue)
        print("hello")
    return highestvalue

print(explorethischange(genpocketchange()))


