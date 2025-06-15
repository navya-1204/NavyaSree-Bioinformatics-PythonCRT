#write a python program to read an integer value as input from the user and print the multiplication table of it
a=int(input("Enter Number:"))
for i in range (1,11):
    print(f"{a} * {i} = {a*i}")
