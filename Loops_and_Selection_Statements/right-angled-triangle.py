"""
Program: right-angled-triangle.py
Author: ALEX KAMAU
CHECKS WHETHER A TRIANGLE IS RIGHT-ANGLED OR NOT
1: The inputs are:
        the sides of the triangle
2: Check whether the triangle is right-angled by using the Pythagorean Theorem:
        if (a**2 + b**2 == c**2)
3: Display the output
"""
# !/usr/bin/env python
a = int(input("Enter the side length: "))
b = int(input("Enter the side length: "))
c = int(input("Enter the side length: "))
if a ** 2 + b ** 2 == c ** 2:
    print("The triangle is right-angled")
else:
    print("The triangle is not Right-angled")
