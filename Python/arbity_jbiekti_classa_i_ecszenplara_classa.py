print("#1 nomber")
class myClass:
    x = 25
    y = 21
    def __init__(self):
        self.z = 10
        self.x = 20
        self.c = 30

d = myClass()
print("self.x =",getattr(d, "x"))
print("myClass.x =",getattr(myClass, "x"))

myClass.x = 26
print("myClass.x =", myClass.x)
print("#1 nomber")
print()

print("#2 nomber")
class myClass1:
    def __init__(self):
        self.z = 26
        self.d = 73
        self.g = "z"

f = myClass1()
print("self.z =", f.z)
print("self.g =", getattr(f,"g"))

d.g = "GGG"
print("self.g =", d.g)
print("#2 nomber")
print()