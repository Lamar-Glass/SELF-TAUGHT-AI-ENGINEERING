# 6th Exercise: Finding area of a circle
#               formular: A = PI * r^2

import math

radius = float(input("Enter your circle's radius: "))
unit = str(input("Enter your unit(cm^2, m^2)"))

area = math.pi * pow(radius, 2)

print(f"Your circle's area is {area}{unit}")
print("THANK YOU FOR USING ME :)")