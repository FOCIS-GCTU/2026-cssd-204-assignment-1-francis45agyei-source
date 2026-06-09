# File: easter_date.py
# Description: Calculates the date of Easter Sunday for a given year.
# Assignment Number: 3
#
# Name: Francis Agyei Asiedu
# SID: YOUR_SID
# Email: YOUR_EMAIL
# Grader: Carolyn
# Slip days used this assignment: 0
#
# On my honor, Francis Agyei Asiedu, this programming assignment is my own work
# and I have not provided this code to any other student.

year = int(input("Enter year: "))

lunar_year_cycle_position = year % 19
weekday_slide_part_1 = year % 4
weekday_slide_part_2 = year % 7

leap_year_100 = year // 100
leap_year_400 = leap_year_100 // 4

lunar_orbit_correction = (13 + 8 * leap_year_100) // 25

century_start = (
    15
    - lunar_orbit_correction
    + leap_year_100
    - leap_year_400
) % 30

sunday_offset = (
    4
    + leap_year_100
    - leap_year_400
) % 7

days_added = (
    19 * lunar_year_cycle_position
    + century_start
) % 30

day_of_week_offset = (
    2 * weekday_slide_part_1
    + 4 * weekday_slide_part_2
    + 6 * days_added
    + sunday_offset
) % 7

total_days_added = 22 + days_added + day_of_week_offset

day_of_easter = total_days_added % 31
month_of_easter = 3 + (total_days_added // 31)

print(
    "In",
    year,
    "Easter Sunday is on",
    str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year) + "."
)