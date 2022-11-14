print("Enter the number:")
x = int(input())
x = 1234

x1 = int(x / 1000)
x2 = int((x / 100) % 10)
x3 = int((x / 10) % 10)
x4 = int(x % 10)
print(x1 + x2 + x3 + x4)