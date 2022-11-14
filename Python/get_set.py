class myClass:
    def __init__(self):
        self.f = 10

    def get_f(self):
        return self.f
    def set_f(self,f):
        self.f = f

d = myClass()
print(d.f)
print()

print(d.get_f())
print()

d.set_f(14)
print(d.get_f())
print()

d.set_f("GGG")
print(d.get_f())
print()

print("f =", getattr(d, "f"))
print()

print("f =", getattr(d, "get_f")())
print()

setattr(d, "f", 40)
print("f =", d.f)
print()