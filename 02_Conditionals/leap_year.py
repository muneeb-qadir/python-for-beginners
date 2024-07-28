year=int(input("Input the year"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is a Leap year")
else:
    print("This is a Normal year")