""" write a python program to create a mobile class and declare the states of mobile as colour , 
price,brand,series,version,features ,storage,battery capacity,processor,ram.Create 10 objects and 
initialize using constructor print the details of the individual objects using function """
class mobile():
    def __init__(self,colour,price,brand,series,version,features,storage,battery_capacity,processor,ram):
        self.colour=colour
        self.price = price
        self.brand = brand
        self.series = series
        self.version = version
        self.features = features          
        self.storage = storage            
        self.battery_capacity = battery_capacity
        self.processor = processor
        self.ram = ram   
def Display_details(self):
    print(f"Colour : {self.colour}")
    print(f"Price  : ₹{self.price:,}")
    print(f"Brand : {self.brand}")
    print(f"Series:{self.series}")
    print(f"Version :{self.version}")
    print(f"Storage : {self.storage}")
    print(f"Battery Capacity : {self.battery_capacity} mAh")
    print(f"Processor : {self.processor}")
    print(f"Features : {self.features}")
    print(f"Ram : {self.ram}")
M1=mobile("Cyan Blue",25000,"IQOO","Z7","1","50MP","512GB","5000MPH","8GB","Snapdragon")
M2=mobile("Black",35000,"Vivo","T5","2","Dualcam","512GB","5000MPH","8GB","Intel")
M3=mobile("White",45000,"Samsung","S27","3","ai","512GB","5000MPH","8GB","Meditech")
M4=mobile("Grey",55000,"GooglePixel","7A","4","pixelcam","512GB","5000MPH","8GB","Snapdragon")
M5=mobile("Blue",65000,"Nokia","10","5","50MP","512GB","5000MPH","8GB","Intel")
M6=mobile("Peach",15000,"Oppo","A3","6","50MP","512GB","5000MPH","8GB","Meditech")
M7=mobile("Pink",75000,"Redmi","9PR0","7","50MP","512GB","5000MPH","8GB","Snapdragon")
M8=mobile("RoseGold",95000,"Oneplus","12A","8","50MP","512GB","5000MPH","8GB","Snapdragon")
M9=mobile("Silver",35000,"Realme","M1","9","50MP","512GB","5000MPH","8GB","Snapdragon")
M10=mobile("cement",15000,"Xiomi","12","10","50MP","512GB","5000MPH","8GB","Snapdragon")
Display_details(M1)
Display_details(M2)
Display_details(M3)
Display_details(M4)
Display_details(M5)
Display_details(M6)
Display_details(M7)
Display_details(M8)
Display_details(M9)
Display_details(M10)