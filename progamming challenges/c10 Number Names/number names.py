while True:
    number = input("input a positive integer a million or less to see how you spell it")
    if 0 <= int(number) < 1000000:
        break
    else:
        print("please enter a positive integer: 0 <= n < 1000000")




def nonzero(number):
    number = str(number)
    while len(number) < 6:
        number += ""
    number = number[::-1]
    print(number)
    wordbank =[]

    if number[1] == "0":
        if number[0] == "1":
            wordbank.append("one")
        elif number[0] == "2":
            wordbank.append("two")
        elif number[0] == "3":
            wordbank.append("three")
        elif number[0] == "4":
            wordbank.append("four")
        elif number[0] == "5":
            wordbank.append("five")
        elif number[0] == "6":
            wordbank.append("six")
        elif number[0] == "7":
            wordbank.append("seven") 
        elif number[0] == "8":
            wordbank.append("eight")
        elif number[0] == "9":
            wordbank.append("nine")

    elif number[1] == "1":
        wordbank.pop()
        if number[0] == "0":
            wordbank.append("ten")
        if number[0] == "1":
            wordbank.append("eleven")
        elif number[0] == "2":
            wordbank.append("twelve")
        elif number[0] == "3":
            wordbank.append("thirteen")
        elif number[0] == "4":
            wordbank.append("fourteen")
        elif number[0] == "5":
            wordbank.append("fifteen")
        elif number[0] == "6":
            wordbank.append("sixteen")
        elif number[0] == "7":
            wordbank.append("seventeen") 
        elif number[0] == "8":
            wordbank.append("eighteen")
        elif number[0] == "9":
            wordbank.append("nineteen")

    if number[1] == "2":
        wordbank.append("twenty")
    elif number[1] == "3":
        wordbank.append("thirty")
    elif number[1] == "4":
        wordbank.append("fourty")
    elif number[1] == "5":
        wordbank.append("fifty")
    elif number[1] == "6":
        wordbank.append("sixty")
    elif number[1] == "7":
        wordbank.append("seventy") 
    elif number[1] == "8":
        wordbank.append("eighty")
    elif number[1] == "9":
        wordbank.append("ninety")
    return wordbank

if number == 0:
    print("zero")
else:
    print(nonzero(number))