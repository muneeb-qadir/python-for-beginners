class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
#functionality
    def full_name(self):
        return f"{self.brand} {self.model}"

#Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

my_tesla = ElectricCar ("Tesla", "Model M", "85KWH")
print(my_tesla.battery_capacity)
print(my_tesla.full_name())

#Basic
my_car = Car("Toyota", "Supra")
print(my_car.brand)
print(my_car.model)
#functionality
print (my_car.full_name())

my_new_car = Car("Nissan", "GTR")
print(my_new_car.brand)

print(my_new_car.model) 