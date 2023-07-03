"""
Program: triangle.py
Author: ALEX KAMAU
CHECKS IF A TRIANGLE IS AN EQUILATERAL OR NOT
1: The inputs are:
        the sides of the triangle
2: Compares the sides of the triangle
        if a=b and b=c
3: Displays the output

"""
# !/usr/bin/env python
a = int(input("Enter the side length: "))
b = int(input("Enter the side length: "))
c = int(input("Enter the side length: "))
if a == b and b == c:
    print("The triangle is an equilateral triangle")
else:
    print("The triangle is not an equilateral triangle")
