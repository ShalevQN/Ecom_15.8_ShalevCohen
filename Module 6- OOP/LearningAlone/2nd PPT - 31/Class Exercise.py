

class Car:
    def __init__(self, brand, color, kilometre, weight, number_of_seats):
        self.__brand = brand
        self.__color = color
        self.__kilometre = kilometre
        self.__weight = weight
        self.__seats= number_of_seats

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def kilometre(self):
        return self.__kilometre

    @kilometre.setter
    def kilometre(self, kilometre):
        self.__kilometre = kilometre

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, seats):
        self.__seats = seats

    def print_info(self):
        print(f"Your car info:\nBrand: {self.__brand}, Color: {self.__color}, Kilometre: {self.__kilometre}, Weight: {self.__weight}, Number of Seats: {self.__seats}")

car1 = Car("Mazda", "red", "150", "1.3", "5")

car2 = Car("Renault", "white", "200", "1.5", "6")

def print_properties_car(car_instance):
    print("Brand:", car_instance.brand)
    print("Color:", car_instance.color)
    print("Kilometre:", car_instance.kilometre)
    print("Weight:", car_instance.weight)
    print("Number of Seats:", car_instance.seats)

print_properties_car(car1)
print_properties_car(car2)

car1.brand = "Toyota"
car1.color = "blue"
car1.kilometre = "10"
car1.weight = "1.2"
car1.seats = "4"

car1.print_info()