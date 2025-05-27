from overrides import overrides
from abc import ABC, abstractmethod

class Moveable(ABC):
    @abstractmethod
    def moveUp(self):
        pass

    @abstractmethod
    def moveDown(self):
        pass

    @abstractmethod
    def moveLeft(self):
        pass

    @abstractmethod
    def moveRight(self):
        pass

class MovablePoint(Moveable):
    def __init__(self, x: int, y: int, x_speed: int, y_speed: int):
        self.__x = x
        self.__y = y
        self.__x_speed = x_speed
        self.__y_speed = y_speed

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def y_speed(self):
        return self.__y_speed

    @y_speed.setter
    def y_speed(self, y_speed):
        self.__y_speed = y_speed

    @property
    def x_speed(self):
        return self.__x_speed

    @x_speed.setter
    def x_speed(self, x_speed):
        self.__x_speed = x_speed

    @overrides
    def moveUp(self):
        self.__y -= self.__y_speed

    @overrides
    def moveDown(self):
        self.__y += self.__y_speed

    @overrides
    def moveLeft(self):
        self.__x -= self.__x_speed

    @overrides
    def moveRight(self):
        self.__x += self.__x_speed

    def __str__(self):
        return f"({self.__x}, {self.__y}) speed=({self.__x_speed}, {self.__y_speed})"