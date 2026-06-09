# File: bowling.py
# Description: Calculates a bowler's average and handicap after three games.
# Assignment Number: 4
#
# Name: Francis Agyei Asiedu
# SID: 2425403399
# Email: francis4agyei@gmail.com
# Grader: Carolyn
# Slip days used in this assignment: 0
#
# On my honor, Francis Agyei Asiedu, this programming assignment is my own work
# and I have not provided this code to any other student.

name = input("Enter your name: ")

game1 = int(input("Enter Game 1: "))
game2 = int(input("Enter Game 2: "))
game3 = int(input("Enter Game 3: "))

average = (game1 + game2 + game3) // 3

handicap = ((200 - average) * 80) // 100

print(name + "'s average is:", average)
print(name + "'s handicap is:", handicap)