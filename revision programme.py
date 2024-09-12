import os
def mainmenu():
  print("\nWelcome to the cs revision program, what do you want to do")
  print("1 - register")
  print("2 - sign in")
  choice = ""
  while choice != "1" and choice != "2":
    choice = input("\n")
    if choice == "1":
      register()
    elif choice == "2":
      signin()
    else:
      print("\nplease select 1 or 2 \n")

def register():
  print("\nYou will be asked for a student name, a username and a password.")
  valid = False
  while valid == False:
    print("\nenter your student name or blank for menu")
    studentname = input()
    if studentname == "":
      valid = True
      mainmenu()
    if len(studentname) >= 1:
      valid = True
  
  valid = False
  while valid == False:
    print("\nenter a unique username, must be 4-8 characters inclusive or blank for menu")
    username = input()
    if username == "":
      valid = True
      mainmenu()
    elif len(username) < 4 or len(username) > 8:
      print("must be 4-8 characters inclusive")
    else:
      f = open("usernames","r")
      userlist = f.readlines()
      f.close()
      for i in range(len(userlist)):
        if userlist[i].strip() == username:
          print("username already exists, try another")
          break
        else:
          valid = True

  valid = False
  while valid == False:
    print("\nenter a password, must be 5+ characters, have a mix of upper/lower characters and numbers or blank for menu")
    password = input()
    checks = 0
    for i in range(len(password)):
      if ord(password[i]) >= 48 and ord(password[i]) <= 57:
        checks = checks + 1 
        break
    for i in range(len(password)):
      if ord(password[i]) >= 65 and ord(password[i]) <= 90:
        checks = checks + 1
        break
    for i in range(len(password)):
      if ord(password[i]) >= 97 and ord(password[i]) <= 122:
        checks = checks + 1
        break
    if password == "":
      valid = True
      mainmenu()
    elif len(password) < 5:
        print("must be 5+ characters")
    elif checks < 3:
      print("password must be a mix of upper/lower and have a number")
    else:
        print("confirm password")
        confirmpassword = input()
        if confirmpassword == password:
          valid = True
      

  f = open("student name", "a")
  f.write("\n")
  f.write(studentname)
  f.close()
  f = open("usernames", "a")
  f.write("\n")
  f.write(username)
  f.close()
  f = open("passwords", "a")
  f.write("\n")
  f.write(password)
  f.close()
  f = open("scores", "a")
  f.write("\n")
  f.write("0")
  f.close()
  print("\n account created!\n")
  mainmenu()
def signin():
  valid = False
  while valid == False:
    print("enter your username or leave blank for menu")
    username = input()
    if username == "":
      valid = True
      mainmenu()
    else:
      f = open("usernames", "r")
      userlist = f.readlines()
      f.close()
      for i in range(len(userlist)):

       if userlist[i].strip() == username:
        valid = True
        break
    if valid == False:
      print("user not found\n")
  
  valid = False
  while valid == False:
    print("\nhello", username, "password please or blank for menu")
    password = input()
    if password == "":
      valid = True
      mainmenu()
    else:
      f = open("passwords", "r")
      passwordslist = f.readlines()
      f.close()
      if passwordslist[i].strip() == password:
        valid = True
        print("welcome\n")
        usermenu(username)
      else:
        print("incorrect password \n")


def usermenu(username):
  print("Welcome to your account", username + ", what do you want to do?")
  print("1 - do some questions!")
  print("2 - look at others' scores")
  print("3 - view account details")
  print("4 - log out \n")
  choice = ""
  while choice != "1" and choice != "2" and choice != "3" and choice != "4":
    choice = input()
    if choice == "1":
      quiz(username)
    elif choice == "2":
      othersscores(username)
    elif choice == "3":
      accountdetails(username)
    elif choice == "4":
      mainmenu()
      
def quiz(username):
  print("welcome to multiple choice", username)
  QandcorrectA = {
    "Selection": "2",
    "LAN": "4",
    "Which protocol is a part of the link layer": "1",
    "What can robotic vampires do?": "3",
    "What is it when someone sends out emails to loads of people hoping that one person clicks for malicious purposes": "4",
    "what is the size of a 4x6 image using 3 colours in bytes": "1"
  }
  answers1 = ["When your program loops", "Lonely Area Network", "Ethernet", "Take over the world", "Fishing", "6"]
  answers2 = ["When your program has to make a choice", "Linked Access Network", "HTTPS", "Smile", "blagging", "9"]
  answers3 = ["when your program chooses what to eat", "Local Amazing Network", "TCP", "Byte", "Pharming", "48"]
  answers4 = ["when your program outputs something", "Local Area Network", "IMAP", "Be peaceful", "Phishing", "72"]
  keylist = list(QandcorrectA.keys())
  score = 0 
  for i in range(len(keylist)):
    keyvalue = keylist[i]
    print("\n", keyvalue)
    print("1 - ", answers1[i])
    print("2 - ", answers2[i])
    print("3 - ", answers3[i])
    print("4 - ", answers4[i])
    useranswer = input()
    if useranswer == QandcorrectA.get(keyvalue):
      score = score + 3
      print("\nyou got it right first try!, 3 points!")
    else:
      print("\nincorrect, another try")
      useranswer = input()
      if useranswer == QandcorrectA.get(keyvalue):
        print("correct, 1 point!")
        score = score + 1
      else:
        print("\n unlucky, the correct answer was", QandcorrectA.get(keyvalue))
  print("\nyou are done!")
  print("final score was", score)
  choice = ""
  while choice != "y" and choice != "n":
    print("\n would you like to save this score? y/n")
    choice = input()
  if choice == "n":
    usermenu(username)
  else:
    savescore(username, score)


def savescore(username, score):
  f = open("usernames", "r")
  usernameslist = f.readlines()
  f.close()
  for i in range(len(usernameslist)):
    if usernameslist[i].strip() == username:
      break
  f = open("scores", "r")
  scoreslist = f.readlines()
  f.close()
  if i == len(usernameslist) - 1:
    scoreslist[i] = str(score)
  else: 
    scoreslist[i] = (str(score) + "\n")
  os.remove("scores")
  f = open("scores", "x")
  f.close()
  f = open ("scores", "a")
  for i in range (len(usernameslist)):
    f.write(scoreslist[i])
  f.close()
  print("done!\n")
  usermenu(username)

def othersscores(username):
  print("\n")
  print("format is: student name, username, score ")
  f = open("student name", "r" )
  studentnameslist = f.readlines()
  f.close()
  f = open("usernames", "r" )
  usernameslist = f.readlines()
  f.close()
  f = open("scores", "r" )
  scoreslist = f.readlines()
  f.close()
  for i in range(len(studentnameslist)):
    print("\n")
    print(studentnameslist[i].strip(), usernameslist[i].strip(), scoreslist[i].strip())
  print("\n")
  usermenu(username)

def accountdetails(username):
  f = open("usernames", "r")
  usernameslist = f.readlines()
  f.close()
  for i in range(len(usernameslist)):
    if usernameslist[i].strip() == username:
      break
  valid = False
  while valid == False:
    print("\nhello", username, "password to view account details or blank to go back")
    password = input()
    if password == "":
      valid = True
      usermenu(username)
    else:
      f = open("passwords", "r")
      passwordslist = f.readlines()
      f.close()
      if passwordslist[i].strip() == password:
        valid = True
        print("\n")
      else:
        print("incorrect password \n")

  f = open("student name", "r")
  studentnameslist = f.readlines()
  f.close()
  f = open("scores", "r" )
  scoreslist = f.readlines()
  f.close()
  print("Student name:", studentnameslist[i].strip())
  print("Username:", username)
  print("Password:", passwordslist[i].strip())
  print("Score:", scoreslist[i].strip())
  print("\n")
  usermenu(username)
  
  
  
  
mainmenu()


