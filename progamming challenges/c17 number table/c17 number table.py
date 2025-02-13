accepted = ["+","-","/","*"]
while True:
    operation = input("input +, -, / or * ")
    if operation in accepted:
        break
while True:
    try:
        number = int(input("input an integer that isnt 0"))
    except:
        print("input an integer")
    else:
        break

firstline = operation + " |"
secondline = "___"
for i in range(0,number+1):
    firstline += " " + str(i)
    secondline+= "__"
print(firstline)
print(secondline)

if operation == "+":
    for g in range(number+1):
        print(g, "|"," ".join([str(number + i) for i in range(number+1)]))
elif operation == "-":
    for g in range(number+1):
        print(g, "|"," ".join([str(number - i) for i in range(number+1)]))
elif operation == "*":
    for g in range(number+1):
        print(g, "|"," ".join([str(number * i) for i in range(number+1)]))
elif operation == "/":
    for g in range(number+1):
        print(g, "|"," ".join([str(number / i) for i in range(number+1)]))
