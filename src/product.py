class Product:
    """
    Класс описывающий свойства и методы сущности
    "Продукт".
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):

        if not isinstance(name, str):
            raise TypeError("name должен быть str")
        if not isinstance(description, str):
            raise TypeError("description должен быть str")
        if type(price) not in [int, float]:
            raise TypeError("price должен быть числом")
        if price <= 0:
            raise ValueError("price должно быть положительным числом")
        if type(quantity) != int:
            raise TypeError("quantity должен быть int")
        if quantity <= 0:
            raise ValueError("quantity должно быть положительным числом")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

