# 5th Exercise: Calculating the circumference of a circle
#               formular is: C = 2*PI*radius

import math

radius = float(input("Please enter the radius of your circle: "))
unit = str(input("Enter the unit(cm, meters): "))

circumference = 2 * math.pi * radius

print(f"And the cirumference of your circle is {round(circumference, 2)}{unit}. ")

print("THANK YOU FOR USING ME :)")
