class Product:
    """
    Класс описывающий свойства и методы сущности
    "Продукт".
    """

    def __init__(
            self, name: str, description: str, price: float, quantity: int
    ):

        if not isinstance(name, str):
            raise TypeError("name должен быть str")
        if not isinstance(description, str):
            raise TypeError("description должен быть str")
        if type(price) not in [int, float]:
            raise TypeError("price должен быть числом")
        if price <= 0:
            raise ValueError("price должно быть положительным числом")
        if type(quantity) is not int:
            raise TypeError("quantity должен быть int")
        if quantity <= 0:
            raise ValueError("quantity должно быть положительным числом")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        if not isinstance(new_price, int | float):
            raise TypeError("new_price должен быть числом")
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > new_price:
            approve_action = input(
                f"Актуальная цена {self.name}: {self.__price}.\n"
                f"Ваша цена ниже актуальной: {new_price}.\n"
                f"Установить предложенную вами цену? y/n\n"
                f"Ответ: "
            )

            if approve_action.lower() == "y":
                self.__price = new_price
            else:
                pass
        else:
            self.__price = new_price

    def __str__(self) -> str:
        return  f"{self.name.capitalize()}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> int | float:
        return (self.price * self.quantity) + (other.price * other.quantity)
