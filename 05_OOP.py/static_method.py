class Car:
    total_car = 0
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model
        self.total_car # We can do this too
        Car.total_car += 1
        #test = Car("Test", "Test") LINE 38


    def get_brand(self):
        return self.__brand + "!"
#functionality
    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Patrol or Diesel"
    @staticmethod
    def gen_description():
        return "Autophile"
#Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def fuel_type(self):
        return "Electric Pulse"
    

# my_tesla = ElectricCar ("Tesla", "Model M", "85KWH")
# 2 underscores can privatize anything that's why following line was giving error Because we can't access private objects outside of Class
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

#Polymorphism
Muneeb = Car("Supra", "MK-4")
MuneebQadir = Car("GTR", "MK-4")
print(Muneeb.fuel_type())
print(Muneeb.total_car)
#test = Car("test","test") Alternative method with the iteration
#print(Car.total_car) We can direct access with the Class name
print(Car.gen_description())