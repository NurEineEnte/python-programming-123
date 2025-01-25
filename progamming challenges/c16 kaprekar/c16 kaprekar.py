number = int(input("input a positive integer to test if it is kaprekar"))
square = str(number **  2)
for i in range(1,len(square)):
    total = int(square[0:i]) + int(square[i:len(square)])
    if total == number:
        print(str(i) + "-kaprekar number")
        break
    elif i == len(square)-1:
        print("not a kaprekar number")