"""
Program: light-year.py
Author: ALEX KAMAU
CALCULATES AND DISPLAYS THE VALUE OF A LIGHT-YEAR
1:The constants are:
        SPEED OF LIGHT = 3 * 10 ** 8 m/s
2:The inputs are:


"""

SPEED_OF_LIGHT = 3 * 10 ** 8 * 5 / 18

no_of_days_in_a_leap_year = 366
no_of_days_in_a_normal_year = 365
no_of_hours_in_a_leap_year = 24 * no_of_days_in_a_leap_year
no_of_hours_in_a_normal_year = 24 * no_of_days_in_a_normal_year

light_year_in_leap_year = SPEED_OF_LIGHT * no_of_hours_in_a_leap_year
light_year_in_a_normal_year = SPEED_OF_LIGHT * no_of_hours_in_a_normal_year

print("The light-year of  a leap year is: ", light_year_in_leap_year, "Km")
print("The light-year of a normal year is: ", light_year_in_a_normal_year, "Km")
