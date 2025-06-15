# write a python program to check whether the user given integer is even or odd using functions
num=int(input("Enter a number:"))
def even_odd(num):
    if num%2==0:
        print(f"{num}is Even")
    else:
        print(f"{num} is Odd")
even_odd(num)
