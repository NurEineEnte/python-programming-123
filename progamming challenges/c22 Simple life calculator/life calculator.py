def VAT():
    while True:
        try:
            price = float(input("input the price of the goods to find VAT"))
        except:
            print("input a price (float/decimal value)")
        else:
            break
    taxedamount = 0.2 * price
    print("the vat added is", taxedamount, "meaning the total is", (taxedamout+price))


def incometax():
    while True:
        try:
            income = float(input("input your annual untaxed income to calculate tax"))
        except:
            print("input your annual income (float/decimal value)")
        else:
            break
    taxes = 0
    if income > 12570:
        basicrate = income - 12570
        if basicrate > 37699:
            basicrate = 37699
            higherrate = basicrate - basicrate
            if higherrate > 74869:
                higherrate = 74869
                addrate = 125140 - higherrate
                taxes += addrate * 0.45
            taxes += higherrate * 0.4
        taxes += basicrate * 0.2
    print("your total taxes add to", taxes")
          
            

def timestable():
    while True:
        try:
            print("hello world")