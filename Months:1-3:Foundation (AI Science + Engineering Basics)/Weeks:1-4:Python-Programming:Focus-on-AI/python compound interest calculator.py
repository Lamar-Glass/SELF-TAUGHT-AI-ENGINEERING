# python compound interest calculator
# using the while loop

currency = "" 
principle = 0
rate = 0
time = 0

while currency == "":
    currency = str(input("Enter your currency ($, CHF, POUNDS, EUROS etc): "))
    if currency == "":
        print("Sorry..i will need your currency type for this.")


while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("ime can't be less than or equal to zero")


# now to check if this code works...
# print(principle)
# print(rate)
# print(time)
# it works..

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: {currency}{total:,.2f}")
                        
