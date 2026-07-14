import pytest

from src.product import Product
from src.category import Category
from src.tools.dataset_handlers import value_packer
from data_for_tests.product_test_data.test_datasets import (
    product_create_valid_data
)


@pytest.fixture(scope='function',
                params=[('Samsung Galaxy S 200', 'Лучшее устройство для лучшей связи', 57000, 23)])
def create_product_valid(request) -> Product:
    name, description, price, quantity = request.param
    return Product(name, description, price, quantity)


@pytest.fixture(scope='function')
def create_category(create_product_valid: Product) -> Category:
    name = 'Устройства связи'
    description = 'Телекоммуникации: рации, станции, смартфоны, спутниковый интернет'
    products =[create_product_valid]
    return Category(name, description, products)
