class Class1:
    def __init__(self, f):
        self.f = f
        print(self.f)

    def f1(self,e):
        self.e = e
        print("Fanc", self.e)

obj1 = Class1('Hello')
obj1.f1("f1")