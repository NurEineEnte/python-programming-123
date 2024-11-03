def caesarcipher(string, shift):
    shiftsleft = 0
    newstring = ""
    for i in range(len(string)):  # about to shift characters or something idk
        shiftsleft = shift
        currentCharValue = ord(string[i].lower())
        if currentCharValue > 96 and currentCharValue < 123:

            while shiftsleft != 0:
                if shiftsleft > 0:
                    shiftsleft = shiftsleft - 1
                    operation = +1
                elif shiftsleft < 0:
                    shiftsleft = shiftsleft + 1
                    operation = -1
                currentCharValue = currentCharValue + operation
                if currentCharValue < 97:
                    currentCharValue = 122
                elif currentCharValue > 122:
                    currentCharValue = 97
            charactertoappend = chr(currentCharValue)
            if string[i] == string[i].upper():
                charactertoappend = charactertoappend.upper()
            newstring = newstring + charactertoappend
    return newstring

print("\nthis caesar cipher shifts letters only, other chars remain constant")
string = input("input a lower/upper case string")
shift = int(input("what shift would you like applied to it"))
print(caesarcipher(string, shift))
