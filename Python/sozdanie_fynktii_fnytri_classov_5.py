class Class:
    def __int__(self):
        pass

    def g1(self):
        print("Hello")
        print()

    def g2(self,f):
        self.f = f
        print("f =", f)
        print()

    def g3(self, s, g, j):
        self.s = s 
        self.g = g
        self.j = j
        print("<s> =", s)
        print("<g> =", g)
        print("<j> =", j)
        print()

    def g4(x):
        x = 10
        if x == 10:
            print("x == 10")
            print("True")
            print()
        else:
            print("x != 10")
            print("False")
            print()

    def g5(self):
            for l in range(0, 5):
                print("100")
                print("200")
                print()

    def g6(s):
        s = 1000-7
        if s == 10:
            print("True")
            print()
        elif s == 20:
            print("False")
            print()
        else:
            print("What")
            print()
 
    def g7(self):
        print("How are you")
        print()

    def g8(self, d, c):
        self.d = d
        self.c = c
        print("d + c =", d + c)
        print("d - c =", d - c)
        print("d * c =", d * c)
        print("d / c =", d / c)
        print()

    def g9(self, e, t, u):
        self.e = e
        self.t = t
        self.u = u
        print("e % e =", e % e)
        print("t % e =", t % e)
        print("u % e =", u % e)
        print()

    def g10(f):
        f = "error"
        if f == "error":
            print("True")
            print()
        else:
            print("False")
            print()

    class Class1:
        def __int__(self):
            pass

    def f1(g):
        g = "7253"
        if g == "7253":
            print("True")
            print()
        else:
            print("False")
            print()

    def f2(self):
        print(".................................")
        print(":                               :")
        print(":           Hello!              :")
        print(":            how                :")
        print(":             a                 :")
        print(":            you                :")
        print(":                               :")
        print(".................................")
        print()

    def f3(x):
        x = 53
        if x == 1:
            print("x == 10")
        elif x == 2:
            print("x = 20")
        elif x == 3:
            print("x = 30")
        elif x == 4:
            print("x = 40")
        else:
            print("False")
            print()

    def f4(d):
        d = 1
        if d == 1:
            print("1")
            print()
        else:
            print("?")
            print()

    def f5(self):
        print("hh.ru")
        print("True")
        print()

    def f6(self, e, r, t, y):
        self.e = e
        self.r = r
        self.t = t
        self.y = y
        print("|e * e| =", e * e)
        print("|r % y * t| =", r % y * t)
        print()

obj1 = Class()
obj1.g1()
obj1.g2("5")
obj1.g3(":s=1:", ":g=2:", ":j=3:")
obj1.g4()
obj1.g5()
obj1.g6()
obj1.g7()
obj1.g8(10, 4)
obj1.g9(2, 3, 4)
obj1.g10()
obj1.f1()
obj1.f2()
obj1.f3()
obj1.f4()
obj1.f5()
obj1.f6(23, 22, 12, 16)