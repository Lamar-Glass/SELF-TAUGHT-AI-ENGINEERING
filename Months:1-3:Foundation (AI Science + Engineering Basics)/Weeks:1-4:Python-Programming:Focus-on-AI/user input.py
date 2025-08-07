# input() = a function that prompt the user to enter data
#           returns the entered data as a string

print("Hello there :)")

name = str(input("Please enter your name: "))
age = int(input("Please enter your age "))
gdp = float(input("And your gdp: "))
is_student = bool(input("Are you still a student(True or False): "))

print(f"Hello there {name}, your are {age} of age and holder of a {gdp} gdp..{is_student} student")