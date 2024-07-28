order_size=input("Enter the Size:")
extra_shot_input=input("Enter T/F")

extra_shot = extra_shot_input.upper() == 'T'

if extra_shot:
    coffee=order_size  + " Coffee with an Extra Shot"
else:
    coffee=order_size + "  Coffee"

    print("Order of: ", coffee)

