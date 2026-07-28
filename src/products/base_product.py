from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass