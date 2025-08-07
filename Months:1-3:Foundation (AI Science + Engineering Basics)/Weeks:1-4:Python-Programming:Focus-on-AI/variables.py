# variables = a container for a value (string, integer, float, boolean)
#             a variable behaves as if it was the value it contains

first_name = str(input("Please enter your name: "))

print(f"Hello {first_name} :)")

# strings
food = "Chapati"
email = "lamar123@fake.com"

print(food + email)

# integers
age = 23
ram = 4

print(f"the age was {age} runing code on a {ram}GB ram laptop")


# floats
quantity = 7.5
pi = 3.146

print(f"The quantity of {food} will be {quantity}. The pi will be {pi} ")

# boolean
is_student = True

if is_student:
    print(f"yeah, Lamar is a student")
else:
    print("he is not a student")    