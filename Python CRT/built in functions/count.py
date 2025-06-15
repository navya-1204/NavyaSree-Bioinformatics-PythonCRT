# write a pyton program to read a string as input from the user 
# >print the count ofuppercase vowels
# >print the count of lower case vowels
# >print the count of uppercase consonants
# >print the count of lowercase consonants
str=input("Enter the string:")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in str:
    if ch.isalpha() and ch.isupper():
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    elif ch.isalpha() and ch.islower():
        if ch in'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Count of upper case vowels:{U_Vowels}")
print(f"Count of lower case vowels:{L_Vowels}")
print(f"Count of upper case consonants:{U_Consonants}")
print(f"Count of lower case consonants:{L_Consonants}")