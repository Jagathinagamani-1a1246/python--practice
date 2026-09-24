#Find the voulme of sphere and cylinder

import math
# Sphere
r = float(input("Enter radius of sphere: "))
sphere_volume = (4 / 3) * math.pi * r ** 3
print("Volume of Sphere =", sphere_volume)

# Cylinder
r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))
cylinder_volume = math.pi * r ** 2 * h
print("Volume of Cylinder =", cylinder_volume)

#Find the Line Equation
x1=float(input("Enter x1 value:"))
y1=float(input("Enter y1 value:"))
m=float(input("slope m value:"))
x=float(input("Enter x value:"))
y = y1+m(x-x1)
print("Y=", y)

# area of a rigth angle triangle --- a = 1/2 * b * h

base = float(input("enter value:"))
height = float(input("Enter value:"))
area = 0.5 * base * height;
print("Area of a right angle triangle:", area)


# area of a circle--- a=pi * r * r

radius = float(input("Enter radius:"))
pi = float(input("enter value:"))
area = pi * radius * radius;
print("Area of a circle:", area)

# area of a circumference --- a =2 * pi * r

radius = float(input("Enter radius:"))
pi = float(input("enter value:"))
area = pi * 2 * radius;
print("Area of a circumference:", area)

#Area of Triangle using Heron's Formula
import math
a = int(input("Enter value:"))
b = int(input("Enter value:"))
c = int(input("Enter value:"))
s =(a+b+c)/2;
area = math.sqrt(s * (s-a) * (s-b) *(s-c))
print("Area of Triangle using Heron's Formula:", area)


