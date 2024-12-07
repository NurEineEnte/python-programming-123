import random
import time
credit = 100
symbols = ["🍒", "🔔", "🍋", "🍊", "⭐", "💀"]
print("👋 welcome to the fruit machine\nyou will start with £1.00 \n- 2 of the same symbol gets you 50p \n- 3 of the same symbol gets you £1\n- 🔔🔔🔔gets you a jackpot (£5)\n- 💀💀 loses you £1\n- 💀💀💀 bankrupts you  ")
print("\n and we shall start with a roll in 5 seconds")
time.sleep(5)
while True:
    skulls = 0
    bells = 0
    same = 0
    symbolcombination = ""
    for i in range(3):
        randomsymbol = symbols[random.randint(0,5)]
        if randomsymbol in symbolcombination and randomsymbol == "💀":
            skulls += 1
        elif randomsymbol in symbolcombination and randomsymbol == "🔔":
            bells +=1
        elif randomsymbol in symbolcombination:
            same += 1
        symbolcombination += randomsymbol
    print(symbolcombination)
    if skulls == 2:
        credit = 0
        print("3 skulls, you lost all your money 🥱")
    elif skulls == 1:
        credit -= 100
        print("oh snappers 2 skulls, you lost yourself £1")
    elif bells == 2:
        credit += 500
        print("3 bells, JACKPOT!!! you won £5!!🎉🎉")
    elif bells == 1 or same == 1:
        credit += 50
        print("two the same, small win! you won 50p ")
    elif same == 2:
        credit += 100
        print("three the same, win! you won £1")
    else:
        print("neutral, no win no lose\n")
    
    print("your current balance is £" + str(credit/100), "\n")

    if credit < 1:
        print("you are bankrupt nerd")
        break
    keepgoing = input("type 'quit' to stop, do anything else to ~~gamble~~ cough i mean play this fun fruit game again")
    if keepgoing.lower() == "quit":
        keepgoing = input("are you sure? did you know that 99 percent of gamblers quit before they hit big?, type 'quit' to confirm")
        if keepgoing.lower() == "quit":
            print("\nyou decided to quit with £" + str(credit/100))
            break