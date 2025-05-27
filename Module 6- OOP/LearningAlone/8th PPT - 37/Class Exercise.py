
class Item:
    def __init__(self, name, group, stock_q, price):
        self.name = name
        self.group = group
        self.stock_q = stock_q
        self.price = price

    def __str__(self):
        return f"This item is {'an ' if self.name[0] in ['a', 'o', 'e', 'u'] else 'a '}{self.name} in the group of {self.group}, we have {self.stock_q} of it. Priced {self.price}$"

    def __hash__(self):
        return hash((self.name, self.group))

    def __repr__(self):
        return f"{self.name}, {self.group} - {self.price}$"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        else:
            if self.name == other.name and self.group == other.group:
                return True
            else:
                return False

item1 = Item("apple", "food", 10, 2.5)
item2 = Item("banana", "food", 2, 4)

item_dict = {item1: item1.stock_q, item2: item2.stock_q}
item3 = Item("apple", "food", 99, 999)
item_dict[item3] = item3.stock_q
print(item_dict)
print(item1)