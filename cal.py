import math

print("What are you going to do? (Multiplication(*), division(/), sum(+), subtraction(-), power (**) or root(R)?")
w = input(" ").upper()
if w == "*" or w == "MULTIPLICATION" or w == "M":
    fn = float(input("Enter the first number: "))
    sn = float(input("Enter the second number: "))
    print(fn * sn)
elif w == "/" or w == "DIVISION" or w == "D":
    fn = float(input("Enter the first number: "))
    sn = float(input("Enter the second number: "))
    print(fn / sn)
elif w == "+" or w == "SUM" or w == "S":
    fn = float(input("Enter the first number: "))
    sn = float(input("Enter the second number: "))
    print(fn + sn)
elif w == "-" or w == "SUBTRACTION" or w == "SU":
    fn = float(input("Enter the first number: "))
    sn = float(input("Enter the second number: "))
    print(fn - sn)
elif w == "**" or w == "POWER" or w == "P":
    fn = float(input("Enter the first number: "))
    sn = float(input("Enter the second number: "))
    print(fn ** sn)
elif w == "R" or w == "ROOT":
    fn = float(input("Enter the number: "))
    print(math.sqrt(fn))
else:
    print("Invalid operation")
