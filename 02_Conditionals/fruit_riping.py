fruit = input("Enter the fruit: ")
color = input("Enter the color: ")

if fruit == "Banana":
    if color == "Green":
        print("Fruit is Unripe")
    elif color == "Yellow":
        print("Fruit is Ripe")
    elif color == "Brown":
        print("Fruit is Overripe")
    else:
        print("Unknown ripeness")
else:
    print("Chose Different Fruit")
