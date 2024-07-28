chars=input("Enter the Password: ")

if len(chars) <= 6:
    strenghth="Weak"
elif len(chars) <= 10:
    strenghth="Moderate"
else:
    strenghth="Strong"
print("Your input Password is: ",strenghth)