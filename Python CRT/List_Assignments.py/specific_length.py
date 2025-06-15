'''
2. Print Items from a List with Specific Length
You are given a list of strings and an integer n. Write a program that prints all the strings 
from the list that have a length exactly equal to n.
'''
List=['NAVYA','RISHI','NIHA','JAYA','JYOTHI','MIDHI']
print(List)
New_list=[]
while(True):
    n=int(input("Enter the length to print the stings in the list : "))
    if(n>len(List)):
        print("Give correct length ")
    else:
        for i in List:
            if len(i) == n:
                New_list.append(i)
        print(New_list)
        break