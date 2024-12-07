import random
import os
def getclassdata(classnum):
    filetoopen = "class" + classnum + ".txt"
    f = open(filetoopen, "r")
    classdata = f.readlines()
    for i in range(len(classdata)):
        classdata[i] = classdata[i].strip()
    f.close()
    return classdata

def getdetails():
    while True:
        print("welcome to the arithmetic test! what class are you a part of, 1/2/3")
        classnum = input()
        if classnum == "1" or classnum == "2" or classnum == "3":
            break
        else:
            print("please type in a valid class number\n")
    print("\nmay i get your name?")
    name = input().lower()
    print("\ngreat! let us get started,", name, "\n")
    score = quiz()
    return (classnum, name, score)

def quiz():
    score = 0
    for i in range(10):
        number1 = random.randint(1,25)
        number2 = random.randint(1,25)
        operation = random.randint(1,4)
        if operation == 1:
            studentanswer = print("What is", number1, "+", number2)
            studentanswer = input()
            answer = number1 + number2
        elif operation == 2:
            studentanswer = print("What is", number1, "-", number2)
            studentanswer = input()
            answer = number1 - number2
        elif operation == 3:
            studentanswer = print("What is", number1//2, "*", number2//2)
            studentanswer = input()
            answer = number1//2 * number2//2
        elif operation == 4:
            studentanswer = print("What is the integer part of", number1, "/", number2)
            studentanswer = input()
            answer = number1 // number2
    
        if studentanswer == str(answer):
            score += 1 
            print("correct answer!\n")
        else:
            print("sorry! the correct answer was", answer)
    print("\nwell done you got", score, "and your scores have been updated\n")
    return score

def bubblesort(list, type):
    passed = True
    if type == "name":
        while passed == True:
            passed = False
            for i in range(0, len(list)-2, 2):
                if list[i] < list[i+2]:
                    list[i], list[i+1], list[i+2], list[i+3] = list[i+2], list[i+3], list[i], list[i+1]
                    passed = True
    elif type == "score":
        while passed == True:
            passed = False
            for i in range(0, len(list)-2, 2):
                if list[i] < list[i+2]:
                    list[i], list[i+1], list[i+2], list[i+3] = list[i+2], list[i+3], list[i], list[i+1]
                    passed = True
    else:
        print("critical error")
    return list

def updatethefile(details, classdata):
    filetoupdate = "class" + details[0] + ".txt"
    os.remove(filetoupdate)
    f = open(filetoupdate, "a")
    for i in range(len(classdata)-1):
        f.write(classdata[i])
        f.write("\n")
    f.write(classdata[len(classdata)-1])
    f.close()

def viewsortedfile():
    while True:
        classnum = input("for which class? 1/2/3")
        if classnum == "1" or classnum == "2" or classnum == "3":
            classdata = getclassdata(classnum)
            classdata = bubblesort(classdata, "score")
            classdata = bubblesort(classdata, "name")
            for i in range(0, len(classdata), 2):
                print(classdata[i], classdata[i+1])   
            break
        else:
            print("input 1 2 or 3 ")

def handlequizdata():
    details = getdetails()
    classdata = getclassdata(details[0])
    countofname = 0
    for i in classdata:
        if details[1] == i:
            countofname += 1
    if countofname == 3:
        for g in range(len(classdata)):
            if details[1] == classdata[g]:
                del classdata[g]
                del classdata[g]
                break
    classdata.append(details[1])
    classdata.append(str(details[2]))
    updatethefile(details, classdata)

while True:
    print("\nwelcome to the arithmetic test menu, what do you want to do")
    print("1 - do the test (student)")
    print("2 - view test scores(teacher)")
    print("quit - stop")
    choice = input()
    if choice == "1":
        handlequizdata()
    elif choice == "2":
        viewsortedfile()
    elif choice.lower() == "quit":
        print("bye bye!!")
        break
    else:
        print("input a valid choice")

