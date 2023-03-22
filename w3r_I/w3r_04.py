# Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math
r = input("Radius=> ")
try:
    r2 = int(r)
except:
    print("Enter a number")

area = math.pi * pow(r2, 2)
print(f"Area = 3.14 x {r2}^2 \n   = 3.14 x {pow(r2,2)} \n   = {round(area,2)}")
