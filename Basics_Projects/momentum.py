"""
Program: momentum.py
Author: ALEX KAMAU
COMPUTES THE MOMENTUM OF AN OBJECT
1:The inputs are :
        mass in kgs
        velocity in m/s
2:The computations are :
        conversion_of_v to km/hr = v * 3.6
        momentum = v * mass
3:The output is :
        momentum


"""

m = float(input("Enter the mass in Kgs: "))
v = float(input("Enter the velocity in m/s: "))

conversion_of_v = v * 5/18
momentum = conversion_of_v * m

print("The momentum of the object is: ", momentum)
