# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = input("Enter your fake credit card number, make sure to space them as it appears on actual card: ")
#credit_number = "1234-5678-9012-3456"

credit_number = credit_number.replace(" ", "-")

print(credit_number)
#print(credit_number[1])
#print(credit_number[0:4]) # always starts from 0
#print(credit_number[5:9])
#print(credit_number[5:]) # this way the code assumes you want everyhting from 5 to last
#print(credit_number[-1]) # with this negative number, it will print the last digit 
#print(credit_number[::2]) # using step, this will print everynumber but will skip every 2 steps.

last_digit = credit_number[-4:] # if i want to print the last 4 digits
reversed = credit_number[::-1] # this will reverse the digits from the last digit to the earlier one.

print(f"XXXX-XXXX-XXXX-{last_digit}")
print(reversed)