class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you ara a graduate now")
# First sub class
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Computer science garduate")
# Second sub class
class Bioinformatics(Graduation):
    @staticmethod
    def Graduate():
        print("Congratulations you are a Bioinformatics garduate")
# Third sub class
class ECE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are an ECE graduate")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()