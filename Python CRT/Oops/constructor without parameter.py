# constructor
class mobile:
    def __init__(self):
        print("Mobile constructor called")
realme = mobile()

class mobile:
    # constructor without parameter
    def __init__(self):
        self.model= 'Realme X'
    def show_model (self):
        print("Model:",self.model)
realme =mobile()
realme.show_model()