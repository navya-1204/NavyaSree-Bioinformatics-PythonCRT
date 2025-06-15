count=int(input("Enter the count data:"))
list=[]
list1=[]
for i in range(count):
    temp=float(input("Enter list:"))
    list.append(temp)
    print(list)
for i in range (count):
    if list[i]<5:
        list1.append("Underexpressed")
    elif list[i]>=5 and list[i]<=15:
        list1.append("Normal")
    else:
        list1.append("Overexpressed")
print(list1)