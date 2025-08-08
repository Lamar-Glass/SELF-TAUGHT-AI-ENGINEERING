# 10th Exercise: Temperature convertor.

print("Hello there, lets begin..")

unit = str(input("Is the temperature in Celsius or Fahrenheit (C/F): "))
temp = float(input("Please enter your temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    unit = "Fahrenheit"
elif  unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    unit = "Fahrenheit" 
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "Celsius"
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "Celsius" 
else:
    print("Sorry it appears i dont have your unit in my programme.")   

print(f"Your converted temperature is {temp}{unit}.") 

rounded = str(input("Would you like it rounded? (Y/N): "))

if rounded == "Y":
    temp = round(temp, 2)
    print(f"Alright: {temp}{unit}")
elif rounded == "y":
    temp = round(temp, 2)  
    print(f"Alright: {temp}{unit}")  
elif rounded == "N":
    print(f"Alright: {temp}{unit}")
elif rounded == "n":
    print(f"Alright: {temp}{unit}")
else:
    print("I dont get that")    

print("THANKS FOR USING ME :) ")

