    # write py prog to check whether the user given number is prime or not using functions (return... keyword)
num=int(input("Enter a number:"))
def prime(Num):
    count=0
    for i in range(1,Num+1):
        if(Num%i==0):
            count+=1
    if (count==2):
        print(f"{Num} is  prime number")
    elif(count==1):
        print(f"{Num} is neither prime nor composite.")
    else:
        print(f"{Num} is not a prime number")
prime(num)