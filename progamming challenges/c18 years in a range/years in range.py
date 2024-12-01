print("years in a range with repeating digits, inclusive")
year1 = input("year 1")
year2 = input("year 2")
yearsintherange = 0

for i in range(int(year1), int(year2)+1):
    year = str(i)
    for x in range(len(year)):
        count = 1
        for y in range(x+1, len(year)-1):
            if year[x] == year[y]:
                yearsintherange+=1
                break
        else:
            continue
        break
print(yearsintherange, "years in the range")