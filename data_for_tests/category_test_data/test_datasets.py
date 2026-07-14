from typing import Any

from src.product import Product

test_product1 = Product("Продукт1", "Описание 1", 1.1, 1)
test_product2 = Product("Продукт2", "Описание 2", 2.2, 2)

category_create_valid_data: list[dict[str, Any]] = [
    {
        "expected_values": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции, "
                           "смартфоны, спутниковый интернет",
            "product_count": 1,
            "category_count": 1,
        }
    }
]

category_create_invalid_data: list[dict[str, Any]] = [
    # Проверка создания категории с отсутствующими
    # параметрами в конструкторе класса
    {
        "data_for_create": {
            "description": "Телекоммуникации: рации, станции,"
                           "смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "Category.__init__() missing 1 required"
                         " positional argument: 'name'",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "Category.__init__() missing 1 required"
                         " positional argument: 'description'",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           "смартфоны, спутниковый интернет",
        },
        "exception_type": TypeError,
        "system_answer": "Category.__init__() missing 1 required"
                         " positional argument: 'products'",
    },
]

category_create_invalid_data_type: list[dict[str, Any]] = [
    {
        "data_for_create": {
            "name": 1,
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": 1.1,
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": True,
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": [1, 2, 3],
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": (1, 2, 3),
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": {1, 2, 3},
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": {"Устройства связи": 1},
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": 1,
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": 1.1,
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": False,
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": [1, 2, 3],
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": (1, 2, 3),
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": {1, 2, 3},
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": {"Устройство": 1},
            "products": [test_product1, test_product2],
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": 1,
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": 1.1,
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": "test_product1",
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": True,
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": (1, 2, 3),
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": {1, 2, 3},
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": {"product": 1},
        },
        "exception_type": TypeError,
        "system_answer": "products должен быть list",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, 1],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, 1.1],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, "1"],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, True],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, [1, 2, 3]],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, (1, 2, 3)],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, {1, 2, 3}],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
    {
        "data_for_create": {
            "name": "Устройства связи",
            "description": "Телекоммуникации: рации, станции,"
                           " смартфоны, спутниковый интернет",
            "products": [test_product1, {"product": 1}],
        },
        "exception_type": TypeError,
        "system_answer": "Не все элементы products"
                         " являются типом Product",
    },
]
