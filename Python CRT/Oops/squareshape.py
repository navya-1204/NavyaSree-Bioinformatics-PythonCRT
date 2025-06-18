"""
Write a python program to create a squareshape class & declare the properties as
Length
Breadth
Height
1) Calculate the Area of square using instance methods
2) Check whether the sides of square's are equal or not using instance methods
3) Calculate the perimeter of square using instance methods
4) Find the diagonals of square using instance methods
5) Find the side length of square using instance methods
"""
class squareshape():
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def Get_area(self):
        print("Area of the shape : ",self.length*self.breadth)
    def Get_square(self):
        print("The shape is square or not : ",self.length==self.breadth)
    def Get_perimeter(self):
        print("The Perimeter of the shape  : ",(2 *(self.length+self.breadth)))
    def Get_diagonal(self):
        print("The Diagnol of permimeter", round((self.length*2 + self.breadth*2) ** 0.5,2) )
    def Get_sidesquare(self):
        print( (self.length) if self.length==self.breadth else "Not Square" )                   
S1=squareshape(5,5,1)
S1.Get_area()
S1.Get_square()  
S1.Get_perimeter()
S1.Get_diagonal()
S1.Get_sidesquare()
print("**************************************************")
S2=squareshape(5,6,1)  
S2.Get_area()
S2.Get_square()  
S2.Get_perimeter()
S2.Get_diagonal()
S2.Get_sidesquare()
