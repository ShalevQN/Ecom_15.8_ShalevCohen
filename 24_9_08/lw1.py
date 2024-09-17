'''
create a python program to calculate how many people fit in how many cars
with how many remainder in the last car.
'''

seats_in_car: int = 5
people_num = int(input("WELCOME!\nA car can contain 5 people.\nWe're going on a trip,"
                       "\nhow many people want to go to the trip?"))

full_cars = people_num // seats_in_car
last_car_people = people_num % seats_in_car


if last_car_people == 0:
    print(f"The road to the trip is going to have {full_cars} full cars.")
elif last_car_people != 0:
    print(f"The road to the trip is going to have {full_cars} full cars and one with {last_car_people} people.")
