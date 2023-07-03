"""
Program: momentum.py
Author: ALEX KAMAU
COMPUTES THE MOMENTUM AND THE KINETIC ENERGY OF AN OBJECT
1:The inputs are :
        mass in kgs
        velocity in m/s
2:The computations are :
        conversion_of_v to km/hr = v * 3.6
        momentum = v * mass
        KE = 0.5 * m * v **2
3:The output is :
        momentum


"""

m = float(input("Enter the mass in Kgs: "))
v = float(input("Enter the velocity in m/s: "))

conversion_of_v = v * 5 / 18
momentum = conversion_of_v * m
KE = 0.5 * m * conversion_of_v ** 2

print("The momentum of the object is: ", momentum)
print("The kinetic energy of the object is: ", KE)
