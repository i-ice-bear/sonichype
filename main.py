print("hello, world")

class Main:
    def __init__(self, _age, _name):
        self.name = _name
        self.age = _age

    def __print__statement(self):
        return f"Name : {self.name}" \
               f"Age : {self.age} "

    def __str__(self):
        return self.__print__statement()


anshu = Main("Anshu", 12)
print(anshu.name)