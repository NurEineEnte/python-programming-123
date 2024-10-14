def pangrams():
    while True:
        string = input("\nplease enter a string to check\n")
        letters = 0
        for i in range(97,123):
            if chr(i) in string or chr(i).upper() in string:
                letters = letters + 1
        if letters == 26:
            print("that is a pangram\n")
        else:
            print("that is not a pangram\n")
        choice = input("continue, y/n?\n")
        if choice == "n":
            break

pangrams()