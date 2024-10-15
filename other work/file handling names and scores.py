import os

def menu1():
    while True:
        try: 
            choice = input("\n 0- exit programme \n 1 - input name and score and add to the file \n 2 - view file contents\n")
            if choice == "0":
                break
            elif choice == "1":
                getdetails()
                writetofile(name,score)
            elif choice == "2" and os.path.exists("scoredata.txt"):
                viewfile()
            else:
                print("invalid, or the file has not yet been created")
        except:
            print("exceptional error found menu1")

def getdetails():
    while True:
        try:
            while True:
                found = False
                global name
                name = input("\nplease input a unique name")
                if os.path.exists("scoredata.txt",):
                    f = open("scoredata.txt", "r")
                    filelist = f.readlines()
                    f.close()
                    for i in range(len(filelist)):
                        if name == filelist[i].strip():
                            found = True
                            print("name already exists")
                            break
                    break
                
            if found == False:
                global score
                score = int((input("please input score")))
                score = str(score)
                if len(name) > 0 and len(score) > 0:
                    break
                else:
                    print("nahhhhhhhhhhhhhhhhhhhhhhhhh mannnn, please type something and have it be unique")
        except:
            print("score must be an integer")

def writetofile(name, score):
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
    global filelist
    filelist = f.readlines()
    f.close()
    for i in range(0, len(filelist), 2):
        print(filelist[i].strip())
    nametolocate =  input("whose score do you want to view").lower()
    for i in range(0, len(filelist), 2):
        if filelist[i].lower().strip() == nametolocate:
            print("the score of", nametolocate, "is", filelist[i+1])
            break
    menu2()

def menu2():
    while True:
        try:
            choice = input("\nwhat would  you like to do? \n 0 - go back to the previous menu \n 1 - delete an item \n 2 - edit a user's  score")
            if choice == "0":
                break
            elif choice == "1":
                deletescore()
            elif choice == "2":
                editscore()

        except:
            print("exceptional error found relating to menu2")

def deletescore():
    usertodelete = input("which user do you want to delete the data for?")
    for i in range(len(filelist)):
        if filelist[i].lower().strip() == usertodelete:
            del filelist[i+1]
            del filelist[i]
            os.remove("scoredata.txt")
            f = open("scoredata.txt", "a")
            f.write(filelist[0].strip())
            for i in range(1, len(filelist)):
                f.write("\n")
                f.write(filelist[i].strip())
            f.close()
            break

def editscore():
    usertoedit = input("which user do you want to edit the score of").lower()
    for i in range(len(filelist)):
        if filelist[i].lower().strip() == usertoedit:
            while True:
                try:
                    newscore = int(input("what score would you like to replace the current one with"))
                except:
                    print("please enter an integer!")
                else:
                    filelist[i+1] = newscore
                    os.remove("scoredata.txt")
                    f = open("scoredata.txt", "a")
                    f.write(filelist[0].strip())
                    for i in range(1, len(filelist)):
                        f.write("\n")
                        f.write(filelist[i].strip())
                    f.close()
                    break


            

        
menu1()
