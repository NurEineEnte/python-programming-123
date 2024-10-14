def logicgates():
    gate = input("OR/AND/XOR/NAND/NOR")
    input1 = input("first input")
    input2 = input("second input")

    if gate.upper() == "OR":
        result = input1 or input2
    elif gate.upper() == "AND":
        result = input1 and input2
    elif gate.upper() == "XOR":
        result = (input1 or input2) and not(input1 and input2)
    elif gate.upper() == "NAND":
        result = not(input1 and input2)
    elif gate.upper() == "NOR":
        result = not(input1 or input2)
    else:
        print("invalid input")
    
    if result == True:
        result = 1
    elif result == False:
        result = 0
    print(result)

logicgates()