import random
from datetime import datetime

class Employee:
    def __init__(self, emp_id, first_name, last_name, address, salary, start_date, pizza_rank, rank_date, pizza_surprise):
        self.__emp_id = emp_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__salary = salary
        self.__start_date = start_date
        self.__pizza_rank = pizza_rank
        self.__rank_date = rank_date
        self.__pizza_surprise = pizza_surprise

    def __repr__(self):
        return f"{self.emp_id} - {self.first_name} {self.last_name}. Rank: {self.rank}"

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, value):
        self.__emp_id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def rank(self):
        return self.__pizza_rank

    @rank.setter
    def rank(self, value):
        self.__pizza_rank = value

    @property
    def rank_date(self):
        return self.__rank_date

    @rank_date.setter
    def rank_date(self, value):
        self.__rank_date = value

    @property
    def pizza_surprise(self):
        return self.__pizza_surprise

    @pizza_surprise.setter
    def pizza_surprise(self, value):
        self.__pizza_surprise = value

    def recalculate_employee_rank(self):
        self.rank = random.randint(1, 100)
        self.rank_date = datetime.now().strftime('%x')

