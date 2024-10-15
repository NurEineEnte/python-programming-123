def getdetails():
    while True:
        try:
            global name
            name = input("\nplease input name")
            global score
            score = int((input("please input score")))
            score = str(score)
            if len(name) > 0 and len(score) > 0:
                break
            else:
                print("nahhhhhhhhhhhhhhhhhhhhhhhhh mannnn, please type something")
        except:
            print("score must be an integer")

def writetofile(name, score):
    print(score)
    try:
        f = open("scoredata.txt", "r")
        f.close()
        f = open("scoredata.txt", "a")
        f.write("\n")
        f.write(name)
        f.write("\n")
        f.write(score)
        
    except:
        f = open("scoredata.txt", "w")
        f.close()
        f = open("scoredata.txt", "a")
        f.write(name)
        f.write("\n")
        f.write(score)
        f.close()

def viewfile():
    print("list of names: \n")
    f = open("scoredata.txt", "r")
    filelist = f.readlines()
    f.close()
    for i in range(0, len(filelist), 2):
        print(filelist[i])
    nametolocate =  input("whose score do you want to view")
    for i in range(0, len(filelist), 2):
        if filelist[i] == nametolocate:
            print("the score of", nametolocate, "is", filelist[i+1])
        
    
    




def menu1():

    while True:
        try:
            
            choice = input("\n 0- exit programme \n 1 - input name and score and add to the file \n 2 - view file contents\n")
            if choice == "0":
                break
            elif choice == "1":
                getdetails()
                writetofile(name,score)
            elif choice == "2":
                viewfile()
            else:
                print("invalid")
        except:
            print("exceptional error found")
            

def menu2():
    while True:
        choice = input("\nwhat would  you like to do? 0 - go back to the previous menu \n 1 - delete an item \n 2 - edit a user's  score")
        if choice == "0":
            break
        
menu1()
