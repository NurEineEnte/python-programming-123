string = input("input a string to check for palindrome")
if string[::-1] == string:
    print("palindrome")
else:
    print("not palindrome")
