def getplate():
    numberplate = input("please enter your number plate, two letters, two numbers then 3 letters like XX77 XXX")

def validateplate(numberplate):  
    if len(numberplate) == 8 and numberplate[0].isalpha() and numberplate[1].isalpha() and numberplate[2].isnumeric() and numberplate[3].isnumeric() and numberplate[5].isalpha() and numberplate[6].isalpha() and numberplate[7].isalpha():
        platevalid = True
    else:
        platevalid = False
    return platevalid

def gettime():
    firsttime = "01234567"
    secondtime = "01234567"
    while len(firsttime) != 8 or firsttime[2] != ":" or firsttime[5] != ":":
        firsttime = input("input the time first camera was passed in 24 hr format HH:MM:SS")
    while len(secondtime) != 8 or secondtime[2] != ":" or secondtime[5] != ":":
        secondtime = input("input the time second camera was passed in 24 hr format HH:MM:SS")

def calculatespeed(firsttime, secondtime):
    firsttimehours = int(firsttime[0]+firsttime[1])+int(firsttime[3]+firsttime[4])/60+int(firsttime[6]+firsttime[7])/3600
    secondtimehours = int(secondtime[0]+secondtime[1])+int(secondtime[3]+secondtime[4])/60+int(secondtime[6]+secondtime[7])/3600
    timeelapsedhours = secondtimehours-firsttimehours
    speedMPH = 1/timeelapsedhours
    speedMPH = round(speedMPH,4)
    return speedMPH

def handletestdatafile():
    f = open("c2testdata.txt", "r")
    firsttime = "00:00:00"
    for i in range(100):
        secondtime = (f.readline()).strip()
        speedMPH = calculatespeed(firsttime,secondtime)
        if speedMPH > 70:
            print(str(speedMPH) + ", broke the speed limit")
        else:
            print(str(speedMPH) + ", good speed")
        numberplate = (f.readline()).strip()
        if validateplate(numberplate) == True:
            print(numberplate , "is a valid plate")
        else:
            print(numberplate , "is invalid")
        print("\n")
    f.close()

handletestdatafile()

