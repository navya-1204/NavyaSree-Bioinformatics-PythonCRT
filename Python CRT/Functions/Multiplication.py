# write a python program to build a function which prints the multiplication table of n 

num=int(input("Enter a number:"))
def table(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
table(num)
