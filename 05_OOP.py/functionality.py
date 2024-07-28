class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
#functionality
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Supra")
print(my_car.brand)
print(my_car.model)
#functionality
print (my_car.full_name())

my_new_car = Car("Nissan", "GTR")
print(my_new_car.brand)

print(my_new_car.model) 