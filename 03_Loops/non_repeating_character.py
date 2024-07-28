str = input("Enter the String ")

for char in str:
    print(str)
    if str.count(char) == 1:
        print("Character is: ",char)
        # break