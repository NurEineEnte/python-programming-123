import os
#os is going to be used for deleting a file when i am changing/deleting data, but for also checking existence

#I have ordered the subroutines below in order of being called (roughly)
#meaning it goes menu1 then getdetails then writetofile and so on
def menu1():
    #starts infinite loop (until it breaks)
    while True:
        try: 
            choice = input("\n 0- exit programme \n 1 - input name and score and add to the file \n 2 - view file contents\n")
            #breaks the loop and thus the programme if 0 is entered
            if choice == "0":
                break
            #this calls the functions to get the user details and write them to the file
            elif choice == "1":
                getdetails()
                writetofile()
            #this one checks if they entered 2, and also if the file exists so that an error doesn't appear
            elif choice == "2" and os.path.exists("scoredata.txt"):
                viewfile()
            #this is a rather broad/general error message
            else:
                print("invalid, or the file has not yet been created")
        #this exception is for if any exceptional errors have been found that i havent fixed
        except:
            print("exceptional error found menu1")

#in summary, this function gets the user name and score before assigining them to their respective global variables
def getdetails():
    #will not stop until both a valid username and score have been entered
    while True:
        try:
            #will not stop until a valid AND unique username has been entered
            while True:
                found = False
                #i used a global variable because i did not want to try returning 2 variables
                global name
                name = input("\nplease input a unique name")

                #this block checks if the username has been used before to avoid issues with repeated names
                #it is possible that the file does not exist at this point
                if os.path.exists("scoredata.txt",):
                    f = open("scoredata.txt", "r")
                    #reads each line of the file into one element of a list each, (noting it still contains whitespace or \n)
                    filelist = f.readlines()
                    f.close()
                    #this loops through the file to check, setting found to true if it isnt unique
                    for i in range(len(filelist)):
                        if name.lower() == filelist[i].strip().lower():
                            found = True
                            print("name already exists")
                            break
                    break

             #this block then asks for the score if the username is unique   
            if found == False:
                global score
                score = int((input("please input score")))
                score = str(score)
                #checks if the user actually entered information for both
                if len(name) > 0 and len(score) > 0:
                    break
                else:
                    print("nahhhhhhhhhhhhhhhhhhhhhhhhh mannnn, please type something and have it be unique")
        # last of all, if it turns out the user entered a non integer for the score then they will be sent through the loop again
        except:
            print("score must be an integer")

#this subroutine used to take name and score as parameters before i made them global, but now takes the variables 
#appends them to the file
def writetofile():
    #this is really nice, because if the file is not readable (doesnt exist), it creates a new file, it also ensures that
    #there isnt an empty line left at the end of the file
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

#this function reads out a list of names in the file, and asks for whose score you want to view
def viewfile():
    print("list of names: \n")
    f = open("scoredata.txt", "r")
    global filelist
    #filelist is now an (unstripped) list of lines of the file
    filelist = f.readlines()
    f.close()
    #this for loop removes whitespace/ the \n character in order to make it a list easy to work with
    for i in range(len(filelist)):
        filelist[i] = filelist[i].strip()
    #prints names and only the names of the people in the file
    for i in range(0, len(filelist), 2):
        print(filelist[i])
    
    #i decided to make it so that names are not case sensitive, hence the use of lower
    nametolocate =  input("whose score do you want to view").lower()
    found = False
    #loops through only the names in the list of the file, until it finds the one the user specified, then breaks
    for i in range(0, len(filelist), 2):
        if filelist[i].lower() == nametolocate:
            print("the score of", nametolocate, "is", filelist[i+1])
            found = True
            break
    #tells the user if the person doesnt exist
    if found == False:
        print("user not in database")
    #opens up a menu for file operations          
    menu2()

#this menu gives the user the choice of going back, deleting an item, or editing data
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
        #i think this was handy back when I was debugging in the reflect and correct lesson
        except:
            print("exceptional error found relating to menu2")

#deletes the users name and score
def deletescore():
    usertodelete = input("which user do you want to delete the data for?")
    #this loop scans the list until it finds the user to delete, then it deletes the index of their name and score, and changes the file
    for i in range(len(filelist)):
        if filelist[i].lower() == usertodelete:
            del filelist[i+1]
            del filelist[i]
            #this deletes the file so it can be made again
            os.remove("scoredata.txt")
            #file created
            f = open("scoredata.txt", "a")
            #first value is appended to the file, to make it so i dont have to deal with where to put \n and not have an empty line!
            f.write(filelist[0])
            for y in range(1, len(filelist)):
                f.write("\n")
                f.write(filelist[y])
            f.close()
            #break ensures that this chunk of code does not repeat
            break

#asks which score they want to edit, what they want to edit it to and changes it
def editscore():
    usertoedit = input("which user do you want to edit the score of").lower()
    for i in range(len(filelist)):
        #loops through the filelist until the user to edit is found
        if filelist[i].lower() == usertoedit:
            #the below code makes sure that the user enters an integer
            while True:
                try:
                    newscore = int(input("what score would you like to replace the current one with"))
                    newscore = str(newscore)
                except:
                    print("please enter an integer!")
                else:
                    #the code in the else statement just changes the list
                    #the line below changes the value corresponding to the name they chose in the list
                    filelist[i+1] = newscore
                    #the below just makes a new file with the updated data again
                    os.remove("scoredata.txt")
                    f = open("scoredata.txt", "a")
                    f.write(filelist[0])
                    for y in range(1, len(filelist)):
                        f.write("\n")
                        f.write(filelist[y])
                    f.close()
                    #... and breaks to exit while true
                    break

#the programme only stops when they navigate to menu1 again and press 0
menu1()
