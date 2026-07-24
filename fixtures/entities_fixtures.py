import pytest
from pytest import FixtureRequest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


# Создается один объект класса Product через конструктор.
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


# Создается один объект класса Product через метод класса new_product.
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


# Создается один объект класса Category через метод конструктор.
@pytest.fixture(scope="function")
def create_category(create_product_valid: Product) -> Category:
    name = "Устройства связи"
    description = (
        "Телекоммуникации: рации, станции, смартфоны, спутниковый интернет"
    )
    products = [create_product_valid]
    return Category(name, description, products)


# Создается три объекта класса Product через конструктор.
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


# Создается один объект класса Smartphone через конструктор.
@pytest.fixture(scope="function")
def create_smartphone() -> Smartphone:
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


# Создается два объекта класса Smartphone через конструктор.
@pytest.fixture(scope="function")
def create_two_smartphone() -> tuple[Smartphone, Smartphone]:
    smartphone1 = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )
    smartphone2 = Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    return smartphone1, smartphone2


# Создается два объекта класса Smartphone и LawnGrass через конструктор.
@pytest.fixture(scope="function")
def create_two_different_products():
    test_smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    test_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    return test_smartphone, test_grass


# Создается один объект класса LawnGrass через конструктор.
@pytest.fixture(scope="function")
def create_lawngrass() -> LawnGrass:
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
