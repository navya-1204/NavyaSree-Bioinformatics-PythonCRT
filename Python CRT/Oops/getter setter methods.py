class mobile():
    def __init__(self,P,C,B):
        self.price=P
        self.color=C
        self.brand=B
        print("Object is Created")
    # Mutator
    def set_color(self):
        self.color='Blue'
    # Accessor
    def Get_Details(self):
        print(f"Colour : {self.color}")
        print(f"Price : {self.price}")
        print(f"Brand : {self.brand}")
M1=mobile(12000,'Black','Samsung')
M1.Get_Details()
print("After Modifying the data : ")
M1.set_color()
M1.Get_Details()
