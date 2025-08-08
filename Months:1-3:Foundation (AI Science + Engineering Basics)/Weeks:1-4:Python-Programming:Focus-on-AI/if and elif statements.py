# if = does some code only IF some conditions is True
#      Elif so this instead
#      Else do something else

age = int(input("Enter your age: "))

if age < 18:
    print("You are a monor")
elif age == 18:
    print("Welcome to adulthood")    
elif age >=18:
    print("You are an adult")   
elif age > 40:
    print("You are old..really old")
else:
    print("Verify your age")
        