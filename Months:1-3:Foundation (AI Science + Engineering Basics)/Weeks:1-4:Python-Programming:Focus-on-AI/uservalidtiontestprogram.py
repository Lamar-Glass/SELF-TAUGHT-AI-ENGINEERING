# THIS IS A USER INPUT VALIDATION EXERCISE.

# Instruction and rules.
# 1. username should not be more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Please enter your username: ")

username.find(" ")

len(username)

if len(username) > 12:
    print("Your username should not be more than 12 characters, please try again.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}. :)")   
