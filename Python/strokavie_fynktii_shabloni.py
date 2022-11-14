s1 = "Hello {0}! I programming {1}. {2}, What {3}?"
print(s1.format("Semen", "Python", "Semen", "Python"))
print()

s1 = "Hello {name}! Я programming {lang}. {name}, What {lang}?"
print(s1.format(name = "Semen",lang = "Python"))
print()

s2 = ('Semen', 'Python')
s3 = ('Ivan', 'Python3')
s1 = "Hello {0[0]}! I programming {0[1]}. {1[0]}, What {1[1]}?"
print(s1.format(s2, s3))
print()

s7 = "int: {0:d}; bin: {0:b}"
print(s7.format(2))
print()

s8 = "23/7 = {0:.3}"
print(s8.format(23 / 7))