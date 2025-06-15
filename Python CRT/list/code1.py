#write a py program to read the str as input from the user
#1) Reverse the string
#2)convert the stn into lowercse
#3) str into uppercase
#4)convert the char of str to lowercase if it is in upper case
#5) convert the char of str to upper case if it is in lowercase
#6)check if the str is starting with the letter a
# 7)print the count of the char a from the give string  and replace all letter p's to letter j
string=input("Enter a string:")
print(string[::-1])
print(string.lower())
print(string.upper())
print(string.swapcase())
print(string.startswith('I'))
print(string.count('p'))
string=string.lower()
print(string.replace('p','j'))