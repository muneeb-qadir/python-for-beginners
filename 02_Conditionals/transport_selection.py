distance = int(input("Enter the Distance: "))
if distance < 3:
    transport= "Walk"
elif distance <=15:
    transport= "Bike"
else:
    transport= "Car"
print("AI recommend you the transport of:",transport)