#compare two strings of the same length and print positions where the sequences differ
sequence1=input("Enter first sequence:")
sequence2=input("Enter second sequence:")
list=[]
if len(sequence1) == len(sequence2):
    for i in range(len(sequence1)):
        if sequence1[i]!=sequence2[i]:
            list.append(i)
    print(list)
else:
    print("Sequences lengths are not same")
