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
        while True:
            line = input("please input 8 characters for colours, consisting of R/G/B/Y").upper()
            if len(line)==8:
                image.append(line)
                break
    return image

def encoder(image):

    encodedimage = []
    for i in range(len(image)):
        encodedstring = ""
        count = 1 
        for x in range(1, len(image[i])):
            if image[i][x] == image[i][x-1]:
                count += 1
                if x == len(image[i])-1:
                    encodedstring += str(count) + image[i][x] 
            else:
                if count == 1:
                    encodedstring += image[i][x-1]
                else:
                    encodedstring += str(count) + image[i][x-1]
                    count = 1
        encodedimage.append(encodedstring)
    return encodedimage

image = encoder(getimage())
for i in range(len(image)):
    print(image[i])
        
    
