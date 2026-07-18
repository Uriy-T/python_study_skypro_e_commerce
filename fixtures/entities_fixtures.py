import pytest
from pytest import FixtureRequest

from src.category import Category
from src.product import Product


@pytest.fixture(
    scope="function",
    params=[
        (
            "Samsung Galaxy S 200",
            "Лучшее устройство для лучшей связи",
            57000,
            23,
        )
    ],
)
def create_product_valid(request: FixtureRequest) -> Product:
    name, description, price, quantity = request.param
    return Product(name, description, price, quantity)


@pytest.fixture(
    scope="function",
    params=[
        (
            "Samsung Galaxy S 200",
            "Лучшее устройство для лучшей связи",
            57000,
            23,
        )
    ],
)
def create_product_by_classmethod(request: FixtureRequest) -> Product:
    params = dict(
        zip(["name", "description", "price", "quantity"], request.param)
    )
    return Product.new_product(params)


@pytest.fixture(scope="function")
def create_category(create_product_valid: Product) -> Category:
    name = "Устройства связи"
    description = (
        "Телекоммуникации: рации, станции, смартфоны, спутниковый интернет"
    )
    products = [create_product_valid]
    return Category(name, description, products)
