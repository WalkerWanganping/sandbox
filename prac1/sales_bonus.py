"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if 0 <= sales < 1000:
        salary = sales * 0.1
    elif 1000 <= sales:
        salary = sales * 0.15
    else:
        salary = "error input"
    print(f"your salary is ${salary} ")
    sales = float(input("Enter sales: $"))
else:
    print("invalid number")
