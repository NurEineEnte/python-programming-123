integer = int(input("input a positive integer to find its factorial"))
total = 1
for i in range(1,integer+1):
    total = total * i
print(total)