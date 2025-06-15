# scenario dna sample
string=input("Enter a string:")
count_A,count_T,count_G,count_C=0,0,0,0
for i in string:
    if i == 'A':
        count_A+=1
    elif i == 'T':
        count_T+=1
    elif i == 'G':
        count_G+=1
    elif i == 'C':
        count_C+=1
    else:
        print(f"{i} is not valid")
dict={'A':count_A,'T':count_T,'G':count_G,'C':count_C}        
print(dict)