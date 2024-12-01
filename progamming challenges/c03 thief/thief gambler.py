import random
#random isnt what you want to see on a pin related programme... but hear me out
# i have done this challenge before, for one of the taster days and this was along the lines
# of my method, i'll explain why it works!

digit1 = int(input("input digit1 "))
digit2 = int(input("input digit2 "))
digit3 = int(input("input digit3 "))
digit4 = int(input("input digit4 "))
count = 0
numOfLists = 0
combinations = []

#count is used to make the probability very favourable
while count <10000:
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
        # if we get a combination not seen before, count resets to 0, otherwise it has
        # to generate 10,000 random combinations before the loop terminates, meaning it is near
        #impossible to miss a combination, the 10,000 can be increased if wanted
print(combinations)
print(numOfLists, "combinations")
#my original programme took a user input for how many digits they wanted to enter and then basically did the same
#whilst making sure that the max number count could be scaled fairly
#this is a pseudo recreation of that 