
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: Division by zero!"
power = num1**5

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Power:", power)