from overrides import overrides
from abc import ABC, abstractmethod

class Employable(ABC):
    @abstractmethod
    def pay_employee(self):
        pass

class Employee(Employable):
    def __init__(self, id, name, email, salary, start_date):
        self.id = id
        self.name = name
        self.email = email
        self.salary = salary
        self.start_date = start_date

    @abstractmethod
    @overrides()
    def pay_employee(self):
        pass


class Developer(Employee):
    def __init__(self, id, name, email, salary, start_date, developer_type, technologies=None):
        super().__init__(id, name, email, salary, start_date)
        self.technologies = technologies if technologies is not None else []
        self.developer_type = developer_type

    @overrides
    def pay_employee(self):
        print(f"Paid {self.name} a salary of {self.salary}.")

    def get_info(self):
        print(f"A {self.developer_type} developer, named {self.name} ID: {self.id}. Started working here {self.start_date} with the salary of {self.salary}. Has technologies {self.technologies}. Contact: {self.email}")

    def learn_technology(self, technology_name):
        self.technologies.append(technology_name)
        print(f"{technology_name} added to {self.name}.")


if __name__ == "__main__":
    dev = Developer(1, "Dana", "dana@example.com", 12000, "2023-01-10", "AI", ["Python", "Git"])
    dev.get_info()
    dev.learn_technology("Docker")
    dev.pay_employee()
