from src.product import Product


class Category:
    """
    Класс описывающий свойства и методы сущности
    "Категория".
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):

        if not isinstance(name, str):
            raise TypeError("name должен быть str")
        if not isinstance(description, str):
            raise TypeError("description должен быть str")
        if not isinstance(products, list):
            raise TypeError("products должен быть list")
        if not all(isinstance(item, Product)for item in products):
            raise TypeError("Не все элементы products являются типом Product")

        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(self.products)
