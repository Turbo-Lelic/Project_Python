class myClass1:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass2(myClass1):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass3:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass4(myClass3):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass5:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass6(myClass5):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass7:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass8(myClass7):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass9:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass10(myClass9):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass11:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass12(myClass11):
    def __init__(self,x):
        self.x=x
        super().__init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass13:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass14(myClass13):
    def __init__(self,x):
        self.x=x
        super(). __init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

class myClass15:
    def __init__(self,x):
        self.x=x
        print("x =",self.x)

class myClass16(myClass15):
    def __init__(self,x):
        self.x=x
        super(). __init__(self.x)
        self.x=10
        print("x =",self.x)
        print()

d = myClass2(23)
d = myClass4(11)
d = myClass6(88)
d = myClass8(99)
d = myClass10(72)
d = myClass12(33)
d = myClass14(22)
d = myClass16(103)