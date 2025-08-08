# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not False, not True)

# or
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")    


# and
age = 23
is_determined = True

if age > 18 and is_determined:
    print("He will become the best self-taught AI-Engineer.")
else:
    print("There is still a time.")   


# not
age = 23
is_determined = True

if age > 18 and not is_determined:
    print("why")
elif age < 18 and not is_determined:
    print("OK")
    
