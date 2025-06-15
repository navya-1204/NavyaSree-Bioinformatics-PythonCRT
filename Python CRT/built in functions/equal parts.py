"""write a python program to read the input from the user 
and split the string into 3 equal halfs using slicing"""
# Read input from the user
text = input("Enter a string: ")

# Check if the string can be divided into 3 equal parts
length = len(text)

if length % 3 == 0:
    size = length // 3
    part1 = text[:size]
    part2 = text[size:2*size]
    part3 = text[2*size:]
    
    print("First part:", part1)
    print("Second part:", part2)
    print("Third part:", part3)
else:
    print("The string cannot be divided into 3 equal parts.")
