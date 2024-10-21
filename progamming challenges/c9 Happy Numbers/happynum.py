
happynumberssequences = []
startingnumber = 1
listofnumbers = []
while len(happynumberssequences) < 8:
    while True:
        startingnumber = str(startingnumber)
        total = 0
        for i in range(len(startingnumber)):
            total = total + int(startingnumber[i]) * int(startingnumber[i])
        
        if startingnumber in listofnumbers:
            listofnumbers.append(startingnumber)
            break
        elif len(listofnumbers) > 1 and listofnumbers[len(listofnumbers)-1] == 1:
            happynumberssequences.append(startingnumber)
            break
        startingnumber = total

        startingnumber += 1