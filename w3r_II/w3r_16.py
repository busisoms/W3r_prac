

import math

a = input("Enter the length of the opposite side (or 'x' if unknown): ")
b = input("Enter the length of the hypotenuse (or 'x' if unknown): ")
c = input("Enter the length of the adjacent side (or 'x' if unknown): ")

if a == "" or b == "" or c == "":
    print("entry can't be empty string")
    quit()

if a.lower() == 'x':
    h = float(b)
    aj = float(c)
    a = math.sqrt(pow(h, 2) - pow(aj, 2))
    print(f"The length of the opposite side is {a}")
elif b.lower() == 'x':
    o = float(a)
    aj = float(c)
    b = math.sqrt(pow(o, 2) + pow(aj, 2))
    print(f"The length of the hypotenuse is {b}")
elif c.lower() == 'x':
    o = float(a)
    h = float(b)
    c_squared = pow(o, 2) - pow(h, 2)
    if c_squared < 0:
        print("Error: Length of adjacent side cannot be calculated with given values.")
    else:
        c = math.sqrt(c_squared)
        print(f"The length of the adjacent side is {c}")
else:
    print("All side lengths are known.")
