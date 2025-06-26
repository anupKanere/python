class Car:
    def __init__(self , brand , name):
        self.__brand = brand # __brand is private variable (Encapsulation)
        self.name = name
    
    @staticmethod
    def car_info():
        return f"BASE PRICE = 1.2 Cr"
    
    def car_details(self):
        return f"Brand -> {self.__brand} and Name -> {self.name}"
    
    # getter method 
    @property
    def get_brand(self):
        return self.brand
    
class ElectricCar(Car):

    def __init__(self, brand, name , fuel):
        super().__init__(brand, name)
        self.fuel = fuel

    # Overriding the car_details method (Inheritance)
    def car_details(self):
        return f"this is child method"
    
def main():
    my_car_one =  Car("BMW" , "X3")
    print(my_car_one.car_details())

    print(Car.car_info()) # calling statis method directly without creating the instance
    


if __name__ == "__main__":
    main()