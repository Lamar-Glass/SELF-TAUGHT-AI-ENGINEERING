# 9th Exercise: weight converter

weight = float(input("Enter your weight: "))
unit = str(input("Is it in kilograms or Pounds? (K OR L): "))

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif  unit == "k":
    weight = weight * 2.205  
    unit = "Lbs"  
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
elif unit == "L":
    weight = weight / 2.205  
    unit = "Kgs"  
else:
    print("Sorry it appears i dont have your unit in my programme.")   

print(f"Your converted weight is {weight}{unit}.") 

rounded = str(input("Would you like it rounded? (Y/N): "))

if rounded == "Y":
    weight = round(weight, 2)
    print(f"Alright: {weight}{unit}")
elif rounded == "y":
    weight = round(weight, 2)  
    print(f"Alright: {weight}{unit}")  
elif rounded == "N":
    print(f"Alright: {weight}{unit}")
elif rounded == "n":
    print(f"Alright: {weight}{unit}")
else:
    print("I dont get that")    

print("THANKS FOR USING ME :) ")



