print("Enter the number: ", end="")
Score = int(input())
print("What ", end="")

if Score >= 0 and Score < 25:
    print("(6)")

if Score >= 25 and Score < 45:
    print("(5)")

if Score >= 45 and Score < 65:
    print("(4)")

if Score >= 65 and Score < 80:
    print("(3)")

if Score >= 80 and Score < 90:
    print("(2)")

if Score >= 90 and Score <= 100:
    print("(1)")

if Score > 100 and Score < 0:
    print("(0)")