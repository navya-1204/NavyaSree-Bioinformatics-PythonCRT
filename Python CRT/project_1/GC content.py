dna_sequence=input("Enter a dna sequence:")
g_count=0
for i in range (len(dna_sequence)):
    if dna_sequence[i]=='G' or dna_sequence[i]=='C':
        g_count+=1
GC_count=(g_count/len(dna_sequence))*100
print(f"GC Content:{GC_count:.2f}%")
if GC_count>60:
    print("High GC content")
elif GC_count<=40:
    print("Less GC content")
else:
    print("Moderate GC content")