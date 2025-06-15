# write a python program to read the list of characters as input from the user and convert it into a word and print it
size=int(input("Enter the size of the list:"))
Char_List=[]
for i in range(size):
    ch=input("Enter the characters:")
    Char_List.append(ch)
print(Char_List)
str="".join(Char_List)
print(str)