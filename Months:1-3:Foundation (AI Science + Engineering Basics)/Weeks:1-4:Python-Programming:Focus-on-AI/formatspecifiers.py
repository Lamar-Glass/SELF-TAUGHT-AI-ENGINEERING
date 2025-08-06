# format specifiers = {:flags} format a value based on what flags are inserted
# format specifiers = {value:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimals places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = to show left allocation
# :> = right justify
# :^ = centre align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# .(number)f = round to that many decimals places (fixed point)
print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")

# :(number) = allocate that many spaces
print(f"price 1 is {price1:10}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:10}")

# :(number) = allocate that many spaces (zero marked spaces/zero padding)
print(f"price 1 is {price1:010}")
print(f"price 2 is {price2:010}")
print(f"price 3 is {price3:010}")

# <: = to show left allocation
print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:<10}")
print(f"price 3 is {price3:<10}")

# >: = to show left allocation
print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")

# :^ = centre align
print(f"price 1 is {price1:^10}")
print(f"price 2 is {price2:^10}")
print(f"price 3 is {price3:^10}")

# :+ = use a plus sign to indicate positive value
print(f"price 1 is {price1:+}")
print(f"price 2 is {price2:+}")
print(f"price 3 is {price3:+}")


print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")

