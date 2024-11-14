def getimage():
    image = []
    while True:
        try:
            numlines = int(input("enter the number of lines for the image to be encoded"))
        except:
            print("please enter an integer")
        else:
            break
    for i in range(numlines):
        image.append()
        while True:
            line = input("please input 8 characters for colours, consisting of R/G/B/Y").upper()
            if len(line)==8:
                for x
                image[i].append(line)
                break
    return image

def encoder(image):
    for i in range(len(image)):
        
    
