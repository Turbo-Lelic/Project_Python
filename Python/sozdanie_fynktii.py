def f1():
    print('Hello')

f1()
print()

def f2(x,y):
    print('x =',x,"  y =",y)

f2(10,12)
print()

def f3(x,y):
    sum = x + y
    print('sum',sum)
    return sum

s = f3(10,20)
print(s)
print()

def f4(x,y,z=0):
    s = x + y + z
    return s

d=f4(10,20,36)
print('d =' , d)
print()

def f5():
    print('Hello')

f5()
print()

def f6(x,d):
    sum = x + d
    print('sum', sum)

f6(10,48)
print()

def f7(v,f):
    sum = v + f
    print('sum', sum)
    return s

s = f7(23,189)
print(s)
print()

def f8(z,f,c,v):
    s1 = "Hello {0}! I programming {1}. {2}, What {3}?"
    print(s1.format(z, f, c, v))
    print(z,f,c,v)

f8('Semen','Python','Semen','C++')
print()

def f10(x):
    if x == 10:
        print("x == 10")
        print("True")
    else:
        print("x != 10")
        print("False")

f10(10)
print()

def f11(l):
    if l == 20:
        print("y == 1")
        print("True")
    else:
        print("y !=")
        print("False")

f11(1)
print()

def f12(x):
    if x == 10:
        print("x == 10")
        print("x == 10")
    elif x == 20:
        print("x = 20")
        print("x == 20")
    elif x == 30:
        print("x = 30")
        print("x == 30")
    elif x == 40:
        print("x = 40")
        print("x == 40")
    else:
        print("False")

f12(10)
print()

def f13(x):
    x == 10
    if x == 10:
        print('f9')
        print('x == True')
    else:
        print('f14')

f13('x')
print()

def f15(x):
    x = 10
    if x == 10:
        print("Good")
    else:
        print("Sad")

f15('x')
print()

def f16(x):
    x = 10
    if x == 10:
        print("How are you")
    elif x == 20:
        print("Good")
    else:
        print("Sad")

f16('x')
print()

def f17(x):
    if x == 23:
     for l in range(0, 5):
        print("G")
        print("O")
        print("O")
        print("D")
        print("!")
        print()

f17(23)
print()