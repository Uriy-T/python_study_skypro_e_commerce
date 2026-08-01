from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict) -> "Product":
        pass

    @property
    @abstractmethod
    def price(self) -> int | float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: int | float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "Product") -> int | float:
        pass
