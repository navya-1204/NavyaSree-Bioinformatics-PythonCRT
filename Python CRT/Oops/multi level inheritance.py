class Grandfather():
    def __init__(self):
        pass
    # Method Overriding
    @staticmethod
    def properties():
        print("100 acres of land")
class Father(Grandfather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def properties():
        print("50 acres of land")
class Yourself(Father):
    def _init_(self):
        super()._init_()
    @staticmethod
    def properties():
        print("Data Analyst")
Grandfather.properties()
Father.properties()
Yourself.properties()
