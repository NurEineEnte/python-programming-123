def getcardnum():
    while True:
        number = input("\nplease input your 16 digit bank card number to validate it format XXXX XXXX XXXX XXXX\n")
        newnumber = ""
        for i in range(len(number)):
            if number[i] != " ":
                newnumber += number[i]
        if len(newnumber) == 16 and newnumber.isnumeric():
            break
        else:
            print("invalid input")
    return newnumber

def luhnAlgorithm(number):
    cardlist = []
    for i in range(len(number)):
        cardlist.append(int(number[i]))
    for i in range(len(cardlist)):
        if i % 2 == 0:
            cardlist[i] *= 2
            currentdigit = str(cardlist[i])
            if len(currentdigit) > 1:
                cardlist[i] = int(currentdigit[0]) + int(currentdigit[1])
    sum = 0
    for i in range(len(cardlist)):
        sum += cardlist[i]
    if sum % 10 == 0:
        print("valid")
    else:
        print("this card has an invalid number!")
        
    

luhnAlgorithm(getcardnum())