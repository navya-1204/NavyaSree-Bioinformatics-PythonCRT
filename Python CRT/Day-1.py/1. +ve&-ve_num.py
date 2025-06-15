"""Write a Python Program to read the integer value as input from the user & check whether it is a positive  
or negative number"""
num=int(input("Enter a number:"))
# if-else
if num>0:
    print(f"{num} is a positive number")
elif num<0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")
#using ternary operator
Res="positive number" if(num>0) else "negative number"
print(f"{num} is a {Res}")