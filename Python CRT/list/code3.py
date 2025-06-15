#write a python program to read mail id as input from the user and print user name and organisation name based on mail id(first:name@orgname.com)
mail_id=input("Enter your mail id:")
list=mail_id.split('@')
print(f"User name:{list[0]}")
org=list[1]
list=org.split('.')
print(f"Org name:{list[0]}")