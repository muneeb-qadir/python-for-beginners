# def add(a,b):
#     sum = a + b
#     sub = a - b
#     return sum, sub

# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")

# sum,sub = add(a,b)
# print("The sum is: ", sum)
# print("The sub is: ", sub)
def cube(num):
    return num**3
cube = lambda x: x**3
print(cube(5))