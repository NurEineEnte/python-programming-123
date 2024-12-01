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
    for j in range(1, len(numarray)):
        nextNum = numarray[j]
        i = j - 1
        while i>=0 and numarray[i]>nextNum:
            numarray[i + 1] = numarray[i]
            i = i - 1       
        numarray[i + 1] = nextNum
    return numarray
num = getnumarray()
print(num)

time1 = time.time()
print(insertionsort(num), "bubble")
print(time.time()-time1)  

time1 = time.time()
print(insertionsort(num), "insertion")
print(time.time()-time1)          
            
        
    

    
 
        
