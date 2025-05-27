from datetime import datetime, timedelta
from employee import Employee
from pizza_hut import PizzaHut
from pizza_dominos import PizzaDominos

emp1 = Employee(
    emp_id=1,
    first_name="Alice",
    last_name="Smith",
    address="123 Main St",
    salary=3000,
    start_date="2023-01-10",
    pizza_rank=75,
    rank_date=(datetime.now() - timedelta(days=2)).strftime('%x'),
    pizza_surprise=None
)

emp2 = Employee(
    emp_id=2,
    first_name="Bob",
    last_name="Jones",
    address="456 Side Rd",
    salary=3200,
    start_date="2022-12-01",
    pizza_rank=60,
    rank_date=(datetime.now() - timedelta(days=1)).strftime('%x'),
    pizza_surprise=None
)

emp3 = Employee(
    emp_id=3,
    first_name="Charlie",
    last_name="Brown",
    address="789 Back Ave",
    salary=2800,
    start_date="2024-04-20",
    pizza_rank=90,
    rank_date=datetime.now().strftime('%x'),
    pizza_surprise=None
)


hut = PizzaHut(1, "Pizza Hut TLV", "Tel Aviv", 2, [emp1, emp2], "03-555-1234", 0)
dominos = PizzaDominos(2, "Pizza Dominos JLM", "Jerusalem", 1, [emp3], "02-444-5678", 0)


hut.hire(emp3)


print(hut)
print(f"Hut Rank: {hut.rank}")
print(dominos)
print(f"Dominos Rank: {dominos.rank}")


print(hut.calculate_employee_expenses(emp1))


surprise = hut.activate_surprise()
emp1.pizza_surprise = surprise

surprise2 = hut.activate_surprise()
emp2.pizza_surprise = surprise2



print("\nBefore ranged rank update:")
for e in hut.employee_list:
    print(e)

hut.calculate_ranged_rank(rank_range=1)

print("\nAfter ranged rank update:")
for e in hut.employee_list:
    print(e)


hut.resign(emp2)
print("\nAfter resignation:")
for e in hut.employee_list:
    print(e)