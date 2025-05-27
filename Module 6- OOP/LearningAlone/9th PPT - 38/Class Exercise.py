import threading
import time

class Customer:
    def __init__(self, id, first_name, last_name, email):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


def send_email(customer):
    print(f"Sending email to {customer.first_name}{customer.last_name} ({customer.email})")
    time.sleep(1)


class EmailThread(threading.Thread):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer

    def run(self):
        try:
            send_email(self.customer)
        except Exception as e:
            print(f"Error sending email: {e}")


customer1 = Customer(1, "Shalev", "Cohen", "shalevch1@gmail.com")
customer2 = Customer(2, "Dana", "Levi", "danalevi2@gmail.com")
customer3 = Customer(3, "Moshe", "Azulay", "mosheazulay3@gmail.com")

customers_list = [customer1, customer2, customer3]

# Sequential version
start_time = time.time()
for customer in customers_list:
    send_email(customer)
end_time = time.time()
execution_time = end_time - start_time
print(f"The function took {execution_time} seconds to execute (sequential).")

# Threaded OOP version
start_time = time.time()
thread_list = []
for customer in customers_list:
    t = EmailThread(customer)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()
end_time = time.time()
execution_time = end_time - start_time
print(f"The function took {execution_time} seconds to execute (threaded).")
