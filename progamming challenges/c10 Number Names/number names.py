while True:
    number = input("input a positive integer a million or less to see how you spell it")
    if 0 < int(number) <= 1000000:
        break
    else:
        print("please enter a positive integer <= 1000000")

number = number[::-1]
print(number)
for i in range(len(number)):
    