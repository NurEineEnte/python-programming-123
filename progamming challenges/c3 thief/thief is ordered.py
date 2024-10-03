permutations = []
listofdigits = []
for i in range(4):
    digittoappend = int(input("enter a digit"))
    listofdigits.append(digittoappend)

for a in range(len(listofdigits)):
    for b in range(len(listofdigits)):
        for c in range(len(listofdigits)):
            for d in range(len(listofdigits)):
                listtotry = []
                if a != b and a != c and a != d and b != c and b !=d and c != d:
                    listtotry = [listofdigits[a], listofdigits[b], listofdigits[c], listofdigits[d]]
                    if listtotry not in permutations:
                        permutations.append(listtotry)

for i in range(len(permutations)):
    print(permutations[i])
print(len(permutations), "permutations")