# while loop = exercute some code WHILE some condition remains true

name = str(input("Enter your name: "))

while name == "":
    print("Hmm..it looks like i didn't get your name...")
    name = str(input("Try entering your name again please: "))
else:
    print(f"Hello {name}, nice to meet you :) ")    

#################################################################

food = str(input("Enter a food you like (q to quit): "))

while not food == "q":
    print(f"You like {food}")
    food = str(input("Enter a food you like (q to quit): "))

print("Tschuss/Bye :)")    

###################################################################

number = int(input("Enter a number between 1-10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a number between 1-10: "))

print(f"Your number is {number}")
   


  