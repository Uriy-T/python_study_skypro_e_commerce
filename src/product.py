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
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> int | float:
        if not isinstance(other, Product):
            raise TypeError(
                f"объект '{other.__class__.__name__}'"
                f" не содержит аттрибута 'price'"
            )
        if type(self) is not type(other):
            raise TypeError(
                f"объект '{other.__class__.__name__}'"
                f" не является '{self.__class__.__name__}'"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int | float,
        color: str,
    ):

        if not isinstance(efficiency, float):
            raise TypeError("efficiency должен быть float")
        if not isinstance(model, str):
            raise TypeError("model должен быть str")
        if type(memory) is not int:
            raise TypeError("memory должен быть int")
        if memory <= 0:
            raise ValueError("memory должно быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("color должен быть str")

        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):

        if not isinstance(country, str):
            raise TypeError("country должен быть str")
        if not isinstance(germination_period, str):
            raise TypeError("germination_period должен быть str")
        if not isinstance(color, str):
            raise TypeError("color должен быть str")

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
