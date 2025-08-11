# indexing = accessing elements of a sequence using []..
#            (indexing operation).
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[2])
print(credit_number[0:3]) # prints numbers from position 0 to 3
print(credit_number[5:9]) # prints numbers from position 5 to 9 
print(credit_number[5:]) # prints numbers from position 5 to end
print(credit_number[-1]) # prints number backwards..the last number starts at -1 not 0
print(credit_number[::2])# prints numbers while skiping after counting"2"

last_digit = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")

