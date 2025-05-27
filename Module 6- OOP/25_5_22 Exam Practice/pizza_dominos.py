from pizza_store_bp import PizzaStore
from overrides import overrides
import random

class PizzaDominos(PizzaStore):
    def __init__(self, store_id, name, address, employee_number, employee_list, phone_number, rank):
        super().__init__(store_id, name, address, employee_number, employee_list, phone_number, rank)

    def __str__(self):
        return "This is a pizza store named pizza dominos, here, they calculate rank as the sum ranks of employees"

    def __repr__(self):
        return "PizzaDominos Class of the PizzaStore BP, has : store_id, name, address, employee_number, employee_list, phone_number, rank"

    @overrides
    def update_rank(self):
        if self.employee_list:
            self.rank = sum(employee.rank for employee in self.employee_list)
        else:
            self.rank = 0