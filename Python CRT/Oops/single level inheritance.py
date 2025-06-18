class vehicle:
    def __init__(self):
        print("I'm the vehicle class constructor")
class car(vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the car class constructor")
    @staticmethod
    def Start():
        print("Car is started.")
C1=car()
C1.Start()
