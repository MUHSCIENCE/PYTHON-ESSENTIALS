"""
Program: minutes.py
Author: ALEX KAMAU
CALCULATES AND PRINTS THE NO. OF MINUTES IN A YEAR
1:The constants are:
        HOUR = 60 MINUTES
        DAY = 24 HOURS
2:The inputs are:
        no of days in the year
3:The computations are:
        number of minutes in year
4:The output is
        number of minutes in a year
"""

no_of_days_in_a_leap_year = 366
no_of_days_in_a_normal_year = 365

no_of_minutes_in_a_leap_year = 60 * 24 * no_of_days_in_a_leap_year
no_of_minutes_in_a_normal_year = 60 * 24 * no_of_days_in_a_normal_year

print("The number of minutes in a leap year is: ", no_of_minutes_in_a_leap_year)
print("The number of minutes in a normal year is: ", no_of_minutes_in_a_normal_year)

exit()
