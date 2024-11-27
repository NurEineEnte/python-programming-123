import random
score = 0
print("welcome to the basic arithmetic test! May i get your name?")
name = input()
while True:
    print("what class are you a part of, 1/2/3")
    classnum = int(input())
    if classnum == 1 or classnum == 2 or classnum == 3:
        break
    else:
        print("please type in a valid class number\n")
    
print("\ngreat! let us get started,", name, "\n")
for i in range(10):
    number1 = random.randint(1,25)
    number2 = random.randint(1,25)
    operation = randomrandint(1,4)
    if operation == 1:
        studentanswer = print("What is", number1, "+", number2)
        studentanswer = input()
        answer = number1 + number2
    elif operation == 2:
        studentanswer = print("What is", number1, "-", number2)
        studentanswer = input()
        answer = number1 - number2
    elif operation == 3:
        studentanswer = print("What is", number1//2, "*", number2//2)
        studentanswer = input()
        answer = number1//2 * number2//2
    elif operation == 4:
        studentanswer = print("What is the integer part of", number1, "/", number2)
        studentanswer = input()
        answer = number1 // number2
    
    if studentanswer == str(answer):
        score += 1 
        print("correct answer!\n")
    else:
        print("sorry! the correct answer was", answer)
print("\nwell done you got", score)

