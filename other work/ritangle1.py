sequences = []
for x in range(1,49):
    for k in range(8,24):
        sequencetotest = [str(x), str(x+k), str(x+2*k), str(x+3*k), str(x+4*k)]
        for i in range(5):
            if len(sequencetotest[i]) < 2:
                sequencetotest[i] = "0" + sequencetotest[i]
        listof10 = []
        found = False
        for i in range(len(sequencetotest)):
            for y in range(len(sequencetotest[i])):
                value = sequencetotest[i][y]

                for z in range(len(listof10)):
                    if len(listof10) > 0 and value == listof10[z]:
                            found = True
                listof10.append(value)
                   
        if found == False:
            for i  in range(len(sequencetotest)):
                sequences.append(sequencetotest[i])
            print(sequencetotest)
total = 0
for i in range(len(sequences)):
    total = total+ int(sequences[i])
print(total)
