# 7th Exercise: Finding the hypothenous of a triagle
#               Formular: a = squareroot(a^2 + b^2)

import math 

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
unit = str(input("Enter your unit(cm, m): "))

hypo = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of your triangle is {hypo}{unit}")
print("THANK YOU FOR USING ME :)")