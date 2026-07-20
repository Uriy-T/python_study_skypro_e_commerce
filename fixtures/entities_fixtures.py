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
            57000.0,
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


@pytest.fixture(
    scope="function",
    params=[
        (
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
        ),
        ("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ],
)
def create_several_products(request: FixtureRequest) -> Product:
    name, description, price, quantity = request.param
    return Product(name, description, price, quantity)
