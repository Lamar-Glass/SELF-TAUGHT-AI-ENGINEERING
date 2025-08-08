# 8th Exercise: Python calculator

operator = str((input("Enter an operator (+ - * /): ")))
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2    
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2    
else:
    print("Sorry i dont have that operator in my programme.")

rounded = str(input("Would you like it rounded to nearest 3? (Y/N): ")) 

if rounded == "Y":
    answer = round(answer, 3)
    print("Rounding to nearest 3..")
elif rounded == "y":
    answer = round(answer, 3)
    print("Rounding to nearest 3..")
else:
    print("No rounding then...")


print(f"The answer to {num1} {operator} {num2} is: {answer}")

print("THANK YOU FOR USING ME :)")

