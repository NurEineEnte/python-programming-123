happynumbers = []
startingnumber = 1
while len(happynumbers) < 8:
    currentnumber = startingnumber
    listofnumbers = []
    while True:
        total = 0
        for i in range(len(str(currentnumber))):
            total += int(str(currentnumber)[i]) ** 2
        if total in listofnumbers:
            break
        elif total == 1:
            happynumbers.append(startingnumber)
            break
        else:
            listofnumbers.append(total)
            currentnumber = total
    startingnumber += 1
print(happynumbers)