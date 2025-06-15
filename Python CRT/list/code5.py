# write a python program to read a string as input from the user 
# >print count of uppercase letters 
# >print count of lowercase letters
# >print count of numeric values
# >print count of special characters
str=input("Enter the string:")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_Char=0
for ch in str:
    if ch.isupper():
        Uppercase_Alpha+=1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():
        Numeric+=1
    else:
        Special_Char+=1
print(f"Count of upper case is:{Uppercase_Alpha}")
print(Lowercase_Alpha)
print(Numeric)
print(Special_Char)
