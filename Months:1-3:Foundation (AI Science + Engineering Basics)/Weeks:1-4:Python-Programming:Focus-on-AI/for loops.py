# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

for x in range(1, 11): # x is a variable, you can change it to anything.
    print(x) # it stopped at 10 not including 11.

print("That was in range function")

for x in reversed(range(1, 11)): # x is a variable, you can change it to anything.
    print(x)

print("This used reversed function to make it count backwards")

for x in range(1, 11, 2): # x is a variable, you can change it to anything.
    print(x) # with adding 2 in the range() it will skip by 2

print("THe output shows it skipped by 2.")

# we can also skip a specific number in the count
# lets skip 13

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
        # you can see the output has no 13 in it.

# you can break a loop by using break.

for x in range(1, 21):
    if x == 13: # the above for loop code has continue..here we replace it with break.
        break
    else:
        print(x)
        # you can see the output has broke leaving us at 12.
