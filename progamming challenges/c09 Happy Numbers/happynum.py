happynumberssequences = []
startingnumber = 1
while len(happynumberssequences) < 8:
    listofnumbers = []
    currentnumber = str(startingnumber)
    while True:
        total = 0
        for i in range(len(currentnumber)):
            total += int(currentnumber[i]) ** 2 
        if total in listofnumbers:
            listofnumbers.append(total)
            break
        elif total == 1:
            happynumberssequences.append(startingnumber)
            break
        else:
            listofnumbers.append(total)
            currentnumber = str(total)
    startingnumber += 1
print(happynumberssequences)