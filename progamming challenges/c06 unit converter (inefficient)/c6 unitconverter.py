def menu():
    while True:
        print("\nWelcome to the unit converter, please make your choice with the numbers below, or leave blank to stop")
        print("1 - temperature")
        print("2 - currency")
        print("3 - volume")
        choice = input()
        if choice == "1":
            temperature()
        elif choice == "2":
            currency()
        elif choice == "3":
            volume()
        elif choice == "":
            break


def temperature():
    while True:
        print("\nplease select your conversion type or leave blank to go back")
        print("1 - K to C")
        print("2 - K to F")
        print("3 - C to K")
        print("4 - F to K")
        print("5 - C to F")
        print("6 - F to C\n")
        choice = input()
        while True:
            try:
                valuetoconvert = float(input("enter your value"))
            except:
                print("enter an number please")
            else:
                print("\n")
                break
        if choice == "":
            break
        elif choice == "1":
            print((valuetoconvert - 273.15), "°C")
            break
        elif choice == "2":
            print(((valuetoconvert - 273.15) * 9/5 + 32), "°F")
            break
        elif choice == "3":
            print((valuetoconvert + 273.15), "K")
            break
        elif choice == "4":
            print(((valuetoconvert - 32) * 5/9 + 273.15), "K")
        elif choice == "5":
            print(((valuetoconvert * 9/5) + 32), "°F")
            break
        elif choice == "6":
            print(((valuetoconvert - 32)* 5/9), "°C")
            break

def currency():
    while True:
        print("\nplease select your conversion type or leave blank to go back")
        print("1 - £ to $")
        print("2 - $ to £")
        print("3 - € to $")
        print("4 - € to £")
        print("5 - £ to €")
        print("6 - $ to €")
        choice = int(input())
        while True:
            try:
                valuetoconvert = float(input("enter your value"))
            except:
                print("enter an number please")
            else:
                print("\n")
                break
        conversiontable = [[1.29, 1/1.29, 1.08, 0.84, 1/0.84, 1/1.08], ["$", "£", "$", "£", "€", "€"]]
        if choice == "":
            break
        else:
            print((valuetoconvert * conversiontable[0][choice-1]), conversiontable[1][choice-1])

def volume():
    while True:
        print("\nplease select your conversion type or leave blank to go back")
        print("1 - cm^3(ml) to dm^3(L)")
        print("2 - dm^3(L) to cm^3(ml)")
        print("3 - cm^3(ml) to m^3")
        print("4 - m^3 to cm^3(ml)")
        print("5 - dm^3(L) to m^3")
        print("6 - m^3 to dm^3(L)")
        choice = int(input())
        while True:
            try:
                valuetoconvert = float(input("enter your value"))
            except:
                print("enter an number please")
            else:
                print("\n")
                break
        conversiontable = [[0.001, 1000, 0.000001, 1000000, 0.001, 1000], ["dm^3(L)", "cm^3(ml)", "m^3", "cm^3(ml)", "m^3", "dm^3(L)"]]
        if choice == "":
            break
        else:
            print((valuetoconvert * conversiontable[0][choice-1]), conversiontable[1][choice-1])
            break

menu()