# format specifiers = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma separator

# .(number)f = round to that many decimal places (fixed point)
print("# .(number)f = round to that many decimal places (fixed point)")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:.2f}")
print(f"price 2 is CHF{price2:.2f}")
print(f"price 3 is CHF{price3:.2f}")

# :(number) = allocate that many spaces
print("# :(number) = allocate that many spaces")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:10}")
print(f"price 2 is CHF{price2:10}")
print(f"price 3 is CHF{price3:10}")

# :03 = allocate and zero pad that many spaces
print("# :03 = allocate and zero pad that many spaces")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:010}")
print(f"price 2 is CHF{price2:010}")
print(f"price 3 is CHF{price3:010}")

# :< = left justify
print("# :< = left justify")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:<10}")
print(f"price 2 is CHF{price2:<10}")
print(f"price 3 is CHF{price3:<10}")

# :< = right justify
print("# :< = right justify")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:>10}")
print(f"price 2 is CHF{price2:>10}")
print(f"price 3 is CHF{price3:>10}")

# :^ = center align
print("# :^ = center align")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:^10}")
print(f"price 2 is CHF{price2:^10}")
print(f"price 3 is CHF{price3:^10}")

# :+ = use a plus sign to indicate positive value
print("# :+ = use a plus sign to indicate positive value")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1:+}")
print(f"price 2 is CHF{price2:+}")
print(f"price 3 is CHF{price3:+}")

# :  = insert a space before positive number
print("# :  = insert a space before positive number")
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is CHF{price1: }")
print(f"price 2 is CHF{price2: }")
print(f"price 3 is CHF{price3: }")

# :, = comma separator
print("# :  = insert a space before positive number")
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"price 1 is CHF{price1:,}")
print(f"price 2 is CHF{price2:,}")
print(f"price 3 is CHF{price3:,}")

# : ALL IN ONE
print("# : ALL IN ONE")
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"price 1 is CHF{price1:+,.2f}")
print(f"price 2 is CHF{price2:+,.2f}")
print(f"price 3 is CHF{price3:+,.2f}")

