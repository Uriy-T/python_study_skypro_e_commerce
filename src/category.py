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
        if not all(isinstance(item, Product) for item in products):
            raise TypeError("Не все элементы products являются типом Product")

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, add_product: Product) -> None:
        if (not isinstance(add_product, Product)
                or not issubclass(type(add_product), Product)):
            raise TypeError("add_product должен быть типом Product")

        for product in self.__products:
            if product.name == add_product.name:
                product.quantity += add_product.quantity
                if add_product.price > product.price:
                    product.price = add_product.price
                break

        else:
            self.__products.append(add_product)
            Category.product_count += 1

    @property
    def products_summary_quantity(self) -> int:
        """
        Вычисляет суммарное количество всех продуктов
        в категории.
        :return: вычисленное количество в формате
        целого числа.
        """
        return sum([product.quantity for product in self.__products])

    @property
    def get_products(self) -> list[str]:
        return [(product.__str__()) for product in self.__products]

    def __str__(self) -> str:
        return (f"{self.name}, количество продуктов:"
                f" {self.products_summary_quantity} шт.")
