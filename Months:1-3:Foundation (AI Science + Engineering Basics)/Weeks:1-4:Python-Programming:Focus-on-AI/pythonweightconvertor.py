# Simple python weight convertor
# it should ask user for input, then conversion unit, then display after calculating.

weight = float(input("Please enter your weight: "))
unit = input("Kilograms or pounds? (KG OR LBS): ")

if unit  == "KG":
    weight = weight * 2.205
    unit = "LBS"
elif unit == "LBS" :
    weight = weight / 2.205
    unit = "KG"   
else:
    print(f"{unit} was invalid, Please update the calculator to current version.")    


print(f"Your weight is: {weight} {unit}: ")