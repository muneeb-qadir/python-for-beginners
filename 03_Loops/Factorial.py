number = int(input("Enter the Number"))
factorial = 1

while number>0:
    factorial *= number
    number -= 1
print("Factorial of a number is", factorial)