class Car: 
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"
#functionality
    def full_name(self):
        return f"{self.brand} {self.model}"

#Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

my_tesla = ElectricCar ("Tesla", "Model M", "85KWH")
# 2 underscores can privatize anything that's why following line was giving error Because we can't access private objects outside of Class
# print(my_tesla.__brand)
print(my_tesla.get_brand())