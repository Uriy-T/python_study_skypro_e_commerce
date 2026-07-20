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
        if not isinstance(add_product, Product):
            raise TypeError("add_product должен быть типом Product")
        for product in self.__products:
            if product.name == add_product.name:
                product.quantity += add_product.quantity
                if add_product.price > product.price:
                    product.price = add_product.price
                break

        else:
            self.__products.append(add_product)
            Category.product_count +=1

    @property
    def get_products(self) -> list[str]:
        return [
            (
                f"{product.name}, {product.price} руб."
                f" Остаток: {product.quantity}"
            )
            for product in self.__products
        ]
