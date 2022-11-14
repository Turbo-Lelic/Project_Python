if 5 in [5, 6, 7, 8, 9, 10]:
    print("this number is in the sequence 5, 6, 7, 8, 9, 10")
    print()

if 1 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and "t" in ["e", "t"]:
    print("this number is in the sequence")
    print()

if 1 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or "r" in ["e", "r"]:
    print("this number is in the sequence")
    print()

if 3 in [1, 2, 3, 4]:
    print("this number is in the sequence 1, 2, 3, 4")
    print()
else:
    print("this number is in the sequence 1, 2, 3, 4")
    print()

if "K1" not in {"K1": 23, "K2": 10}:
    print("the given word is in the sequence")
    print()

if 5 not in [5, 6, 7, 8, 9, 10]:
    print("this number is in the sequence 5, 6, 7, 8, 9, 10")
    print()

if 1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and "t" not in ["e", "t"]:
    print("this number is in the sequence")
    print()

if 1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or "r" not in ["e", "r"]:
    print("this number is in the sequence")
    print()

if 3 not in [1, 2, 3, 4]:
    print("this number is in the sequence 1, 2, 3, 4")
    print()
else:
    print("this number is in the sequence 1, 2, 3, 4")
    print()

if "K1" not in {"K1": 23, "K2": 10}:
    print("the given word is in the sequence")
    print()

x = y = [1, 2]
print(x is y)
print(x, y)
x[0] = 23
print(x, y)
print()

c = v = [5, 10]
print(c, v)
c[0] = 55
v[1] = 53
print(c, v)
print()

a, s = [12, 22], [11, 33]
print(a, s)
a[0] = 24
a[1] = 99
s[0] = 57
s[1] = 77
print(a, s)