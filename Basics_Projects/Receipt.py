"""
Program: Receipt.py
Author: ALEX KAMAU
Computes the total charge for a customer's video rentals
1: Significant constants:
        NEW_ARRIVALS = 3.00
        OLDIES = 2.00
2: The inputs are:
           numberOfNights
           numOfNewTapes
           numOfOldies
3: Computations are:
            costOfNewArrivals = NEW_ARRIVALS * numOfNewTapes * numberOfNights
            costOfOldies = OLDIES * numOfOldies * numberOfNights
            totalCharges = costOfNewArrivals + costOfOldies
4: The output is:
            totalCharges

"""

NEW_ARRIVALS = 3.00
OLDIES = 2.00

numberOfNights = int(input("Enter the number of nights: "))
numOfNewTapes = int(input("Enter the number of New tapes: "))
numOfOldies = int(input("Enter the number of old tapes: "))

costOfNewArrivals = NEW_ARRIVALS * numOfNewTapes * numberOfNights
costOfOldies = OLDIES * numOfOldies * numberOfNights

totalCharges = costOfNewArrivals + costOfOldies
print("The total charges are $", totalCharges)
