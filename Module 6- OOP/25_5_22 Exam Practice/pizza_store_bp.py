from abc import ABC, abstractmethod
import random
from datetime import datetime
import copy

class Surprise:
    def __init__(self, description):
        self.description = description

    def activate_surprise(self):
        print("You got a surprise! Congratulations!")
        print(f"🎁 {self.description}")


class PizzaStore(ABC):
    def __init__(self, store_id, name, address, employee_number, employee_list, phone_number, rank):
        self.__store_id = store_id
        self.__name = name
        self.__address = address
        self.__employee_number = employee_number
        self.__employee_list = employee_list
        self.__phone_number = phone_number
        self.__rank = rank
        self.surprise_stock = [
            Surprise("Free pineapple 🍍"),
            Surprise("Dance break 🕺"),
            Surprise("Box folds into fort 🏰"),
            Surprise("Dough fight 🍞"),
            Surprise("Opera order 🎤"),
            Surprise("Chef-signed slice ✍️"),
            Surprise("Dino delivery 🦖"),
            Surprise("Mystery topping 🤔"),
            Surprise("Box joke 😅"),
            Surprise("Sneaky double cheese 🧀"),
            Surprise("Extra napkin"),
            Surprise("2% sock coupon"),
            Surprise("Pizza facts"),
            Surprise("One olive bagged"),
            Surprise("Far car wash flyer"),
            Surprise("QR to QR"),
            Surprise("Blank sticky note"),
            Surprise("Receipt typo"),
            Surprise("Room-temp slice")]

    def __str__(self):
        return "This is a blueprint of the pizza stores."

    @property
    def store_id(self):
        return self.__store_id

    @store_id.setter
    def store_id(self, store_id):
        self.__store_id = store_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def employee_number(self):
        return self.__employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        self.__employee_number = employee_number

    @property
    def employee_list(self):
        return self.__employee_list

    @employee_list.setter
    def employee_list(self, employee_list):
        self.__employee_list = employee_list
        self.update_rank()

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    @property
    def surprise_stock(self):
        return self.__surprise_stock

    @surprise_stock.setter
    def surprise_stock(self, surprises_stock):
        self.__surprise_stock = surprises_stock

    def calculate_employee_expenses(self, employee):
        return f"Employee expenses are {self.employee_number * employee.salary}"

    def hire(self, employee):
        if employee in self.employee_list:
            print("The employee is already working here!")
        else:
            self.employee_list.append(employee)
            self.update_rank()

    def resign(self, employee):
        if employee in self.employee_list:
            if employee.pizza_surprise:
                surprise_taken = employee.pizza_surprise
                self.surprise_stock.append(surprise_taken)
            self.employee_list.remove(employee)
            self.update_rank()
        else:
            print("The employee is not working here!")


    @abstractmethod
    def update_rank(self):
        pass

    def activate_surprise(self):
        current_surprise = random.choice(self.surprise_stock)
        self.surprise_stock.remove(current_surprise)
        surprise_copy = copy.deepcopy(current_surprise)
        surprise_copy.activate_surprise()
        return surprise_copy

    def calculate_ranged_rank(self, rank_range):
        for employee in self.employee_list:
            current_rank_emp = datetime.strptime(employee.rank_date, "%x")
            difference = (datetime.now() - current_rank_emp).days
            if difference > rank_range:
                employee.recalculate_employee_rank()
        self.update_rank()
