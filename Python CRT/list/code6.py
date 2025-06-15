# write a python program to take name as input from the user including prefix(Mr/Miss)
# print the gender classification of the name on basis of prefix     
str=input("Enter name:")
# if str.startswith('Mr.'):
#     print("Male")
# else:
#     print("Female")
if (str[0:2]==('Mr.')):
    print("Male")
else:
    print("Female")