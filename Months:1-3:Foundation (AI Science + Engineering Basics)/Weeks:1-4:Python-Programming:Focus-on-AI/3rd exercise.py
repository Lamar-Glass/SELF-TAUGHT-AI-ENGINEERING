# 3rd Exercise: shopping cart program

print("SHOPPING CART")

item = str(input("Please enter desired item: "))
cost = float(input("What is the cost of the one item: "))
currency = str(input("And what currency would you use($, CHF): "))
quantity = int(input("How many would you like: "))

total = cost * quantity

print(f"Just to confirm you want {quantity} X of {item} worth the cost of {cost} each...")
print(f"That will sum up to {currency} {total}.")

print("THANK YOU FOR USING ME :)")

