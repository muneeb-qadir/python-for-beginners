
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

adult_price = 12
child_price = 8
discount = 2

if age < 13:
    base_price = child_price
else:
    base_price = adult_price

if day == "Wednesday":
    final_price = base_price - discount
else:
    final_price = base_price


print("The ticket price is $", final_price)
