pet = input("Enter the pet: ")
age = int(input("Enter the age: "))

if pet == "Dog":
    if age < 2:
        print("Puppy Food")
elif pet == "Cat":
    if age > 5:
        print("Senior Cat Food")
else:
    print("Invalid Input")