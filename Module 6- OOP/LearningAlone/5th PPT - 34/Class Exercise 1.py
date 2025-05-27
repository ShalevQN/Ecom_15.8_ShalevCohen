from overrides import overrides

class Chair:
    def __init__(self, model, number_of_legs, price):
        self.__model = model
        self.__number_of_legs = number_of_legs
        self.__price = price

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def number_of_legs(self):
        return self.__number_of_legs

    @number_of_legs.setter
    def number_of_legs(self, number_of_legs):
        self.__number_of_legs = number_of_legs

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def print_chair(self):
        print(f"Chair model is {self.model}, has {self.number_of_legs} priced {self.price}$.")

    def calculate_price(self, number_of_chairs):
        total = self.price * number_of_chairs
        return f"Total price for {number_of_chairs} chairs: ${total}"

class GamingChair(Chair):
    #@overrides
    def __init__(self, model, number_of_legs, price, allow_adjustments: bool, is_spinning: bool, has_discount: bool, discount_amount: int):
        super().__init__(model, number_of_legs, price)
        self.__allow_adjustments = allow_adjustments
        self.__is_spinning = is_spinning
        self.__has_discount = has_discount
        self.__discount_amount = discount_amount

    @property
    def allow_adjustments(self):
        return self.__allow_adjustments

    @allow_adjustments.setter
    def allow_adjustments(self, allow_adjustments):
        self.__allow_adjustments = allow_adjustments

    @property
    def is_spinning(self):
        return self.__is_spinning

    @is_spinning.setter
    def is_spinning(self, is_spinning):
        self.__is_spinning = is_spinning

    @property
    def has_discount(self):
        return self.__has_discount

    @has_discount.setter
    def has_discount(self, has_discount):
        self.__has_discount = has_discount

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self.__discount_amount = discount_amount

    @overrides
    def print_chair(self):
        super().print_chair()
        print(f"Adjustable: {self.allow_adjustments}")
        print(f"Spinning: {self.is_spinning}")
        print(f"Has discount: {self.has_discount}")
        print(f"Discount amount: {self.discount_amount}%")

    @overrides
    def calculate_price(self, number_of_chairs):
        if self.__has_discount:
            total = self.price * number_of_chairs * (1- (self.__discount_amount / 100))
        else:
            total = self.price * number_of_chairs
        return f"Total price for {number_of_chairs} chairs: ${total}"

class OfficeChair(Chair):
    #@overrides
    def __init__(self, model, number_of_legs, price, allow_adjustments: bool, is_spinning: bool, has_discount: bool, discount_amount: int):
        super().__init__(model, number_of_legs, price)
        self.__allow_adjustments = allow_adjustments
        self.__is_spinning = is_spinning
        self.__has_discount = has_discount
        self.__discount_amount = discount_amount

    @property
    def allow_adjustments(self):
        return self.__allow_adjustments

    @allow_adjustments.setter
    def allow_adjustments(self, allow_adjustments):
        self.__allow_adjustments = allow_adjustments

    @property
    def is_spinning(self):
        return self.__is_spinning

    @is_spinning.setter
    def is_spinning(self, is_spinning):
        self.__is_spinning = is_spinning

    @property
    def has_discount(self):
        return self.__has_discount

    @has_discount.setter
    def has_discount(self, has_discount):
        self.__has_discount = has_discount

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self.__discount_amount = discount_amount

    @overrides
    def print_chair(self):
        super().print_chair()
        print(f"Adjustable: {self.allow_adjustments}")
        print(f"Spinning: {self.is_spinning}")
        print(f"Has discount: {self.has_discount}")
        print(f"Discount amount: {self.discount_amount}%")

    @overrides
    def calculate_price(self, number_of_chairs):
        if self.__has_discount:
            total = self.price * number_of_chairs * (1- (self.__discount_amount / 100))
        else:
            total = self.price * number_of_chairs
        return f"Total price for {number_of_chairs} chairs: ${total}"