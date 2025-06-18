'''
write a python program to create a product class declare the states of the class as productname, 
productid, price,GST,mfdate,expdate
1) Create 5 objects initialize it using parameterized constructor and access them using instance method 
2) Declare mutator methods as set.objects given and change the values of their properties 
using mutators methods and print it 
'''
class product():
    def __init__(self,productname,productid,price,GST,mfdate,expdate):
        self.productname=productname
        self.productid=productid
        self.price=price
        self.GST=GST
        self.mfdate=mfdate
        self.expdate=expdate
        print("Object is Created")
    def set_Details(self):
        self.productname="biscuit"
        self.productid='pd03'
        self.price=50
        self.GST='10%'
        self.mfdate="15/6/25"
        self.expdate="16/9/2025"
        # Accessor
    def Get_Details(self):
        print(f"Product Name : {self.productname}")
        print(f"Product ID : {self.productid}")
        print(f"Price : {self.price}")
        print(f"GST:{self.GST}")
        print(f"MF date:{self.mfdate}")
        print(f"EXP date:{self.expdate}")
P1=product("Dairy milk","pd1",100,"15%","27/6/25","14/10/25")
P1.Get_Details()
print("*******************")
P1.set_Details()
P1.Get_Details()