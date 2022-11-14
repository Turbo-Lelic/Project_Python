class Class1:
    def __init__(self):
        self.a = 10
        self.s = 20

    def get_a(self):
        return self.a

    def set_a(self,a):
        self.a = a

    def get_s(self):
        return self.s

    def set_s(self,s):
        self.s = s

d = Class1()
print(d.a)
print(d.get_a())
d.set_a(27)
print(d.get_a())
d.set_a("SUS")
print(d.get_a())
print("a =", getattr(d, "a"))
print("a =", getattr(d, "get_a")())
setattr(d, "a", 40)
print("a =", d.a)
print()
print(d.s)
print(d.get_s())
d.set_a(27)
print(d.get_s())
d.set_a("sss")
print(d.get_s())
print("s =", getattr(d, "s"))
print("s =", getattr(d, "get_s")())
setattr(d, "s", 40)
print("s =", d.s)
print()