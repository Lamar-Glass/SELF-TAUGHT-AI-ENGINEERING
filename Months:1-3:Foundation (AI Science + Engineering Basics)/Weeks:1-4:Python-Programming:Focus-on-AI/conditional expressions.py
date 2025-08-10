# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          X if condition else Y

number = float(input("Enter an random number(-1,7,-100): "))
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor!"

print("Positive-side-Number" if number > 0 else "Negative-Side-Number")