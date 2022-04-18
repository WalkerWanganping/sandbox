items_price = []
total_price = 0
items_number = int(input("enter item number"))
for i in range(1,items_number+1):
    items_price.append(input("enter item price:$"))
print(f"Number of items: {items_number}")


for i in range(0,items_number):
    print(f"Price of item:${items_price[i]}")


for i in range(0,items_number):
    total_price += int(items_price[i])
print(f"total price:${0.9*total_price}")

