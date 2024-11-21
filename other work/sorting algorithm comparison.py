import random
import time
def getnumarray():
    numarray = []
    for i in range(10):
        numarray.append(random.randint(1,50))
    return numarray

def bubblesort(numarray):
    while True:
        swapsmade = False
        for i in range(len(numarray)-1):
            if numarray[i] > numarray[i+1]:
                numarray[i], numarray[i+1] = numarray[i+1], numarray[i]
                swapsmade = True
        if swapsmade == False:
            break
    return numarray

def insertionsort(numarray):
    for i in range(1, len(numarray)-1):
        numtoplace = numarray[i]
        for j in range(i-1):
            if numtoplace <= numarray[j]:
                break
            elif numtoplace > numarray[j] and j == i-1:
                j = i+1
        for x in range(j, len(numarray)-1):
            numarray[x], numtoplace = numtoplace, numarray[x]
    return numarray
print(insertionsort(getnumarray()))
            
            
        
    

    

        
