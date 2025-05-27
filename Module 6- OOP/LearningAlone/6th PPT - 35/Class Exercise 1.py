from overrides import overrides
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def greet(self):
        pass

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print("meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @overrides
    def greet(self, another= None):
        if isinstance(another, Dog):
            print("woooof")
        else:
            print("woof")

class BigDog(Animal):
    def __init__(self, name):
        super().__init__(name)
    @overrides
    def greet(self, another=None):
        if isinstance(another, Dog):
            print("Woooooo")

        elif isinstance(another, BigDog):
            print("Woooooow")

        else:
            print("Wooow")

cat = Cat("Cat")
dog1 = Dog("Dog1")
dog2 = Dog("Dog2")
bigdog1 = BigDog("BigDog1")
bigdog2 = BigDog("BigDog2")

cat.greet()
dog1.greet()
dog1.greet(dog2)
bigdog1.greet()
bigdog1.greet(dog1)
bigdog1.greet(bigdog2)

