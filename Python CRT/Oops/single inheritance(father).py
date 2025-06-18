class Father:
    def _init_(self):
        pass
    @staticmethod
    def work():
        print("Hardworking father")
class Son(Father):
    def _init_(self):
        super()._init_()
    @staticmethod
    def work():
        print("Enjoy")
Father.work()
Son.work()