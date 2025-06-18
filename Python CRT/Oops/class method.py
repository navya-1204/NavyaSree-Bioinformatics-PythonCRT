class Mobile:
    def _init_(self):
        print("Object is created")
    @classmethod
    def Display(Class):
        print("I'm a Class Method")
        print("I will work irrespective of object creation")
Mobile.Display()
M1=Mobile()
M1.Display()