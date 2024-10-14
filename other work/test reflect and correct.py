def getdetails():
    while True:
        try:
            global name
            name = input("please input name")
            global score
            score = int((input("please input score")))
            score = str(score)
            if len(name) > 0 and len(score) > 0:
                break
            else:
                print("nuh uh, please type something")
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

        



getdetails()
writetofile(name, score)
print(name, score)