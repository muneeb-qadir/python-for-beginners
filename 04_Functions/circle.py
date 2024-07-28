import math
def circle_stats(radius):
    area=math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference
radius = float(input("Enter the value of r: "))

area,circumference = circle_stats(radius)

print("The area of the circle is: ", area, "\nThe Circumference of a circle is: ",circumference)