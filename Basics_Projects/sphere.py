"""
Program: sphere.py
Author: ALEX KAMAU
COMPUTES THE DIAMETER, CIRCUMFERENCE, SURFACE AREA AND VOLUME OF A SPHERE
1: The input is:
            Radius, r
2: Compute the following:
        Diameter, d = 2*r
        Circumference, c = pi*d
        Surface Area, sA = 4/3*pi*r**2
        Volume, v = 4/3*pi*r**3
3: The outputs are:
            Diameter
            Circumference
            Surface Area
            Volume
"""
from math import pi

r = float(input("Enter the radius: "))

d = 2 * r
c = pi * d
sA = 4 / 3 * pi * r ** 2
v = 4 / 3 * pi * r ** 3

print("The diameter of the sphere is ", d)
print("The circumference of the sphere is ", c)
print("The surface area of the sphere is ", sA)
print("The volume of the sphere is ", v)
