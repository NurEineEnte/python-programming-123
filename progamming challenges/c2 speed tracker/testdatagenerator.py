#you may want to change the name of the file accessed in this code!
import random
for i in range(100):
    time = ""
    time = time + str(random.randint(0,0))
    time = time + str(random.randint(0,0))
    time = time + ":"
    time = time + str(random.randint(0,0))
    time = time + str(random.randint(0,9))
    time = time + ":"
    time = time + str(random.randint(0,5))
    time = time + str(random.randint(0,9))
    print(time)

    plate = ""
    plate = plate + chr(random.randint(65,90))
    plate = plate + chr(random.randint(65,90))
    plate = plate + str(random.randint(0,13))
    plate = plate + str(random.randint(0,9))
    plate = plate + " "
    plate = plate + chr(random.randint(65,90))
    plate = plate + chr(random.randint(65,90))
    plate = plate + chr(random.randint(65,90))
    print(plate)
    #here
    f = open("c2testdata.txt", "a")
    f.write(time)
    f.write("\n")
    f.write(plate)
    f.write("\n")
    f.close()