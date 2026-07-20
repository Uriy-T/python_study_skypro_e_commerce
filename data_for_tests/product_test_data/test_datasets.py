from typing import Any

product_create_valid_data: list[dict[str, Any]] = [
    {
        "create_product": {
            "name": "Samsung Galaxy S 200",
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000,
            "quantity": 23,
        },
        "expected_values": {
            "name": "Samsung Galaxy S 200",
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000.00,
            "quantity": 23,
        },
    },
    {
        "create_product": {
            "name": "Nintendo Switch",
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "expected_values": {
            "name": "Nintendo Switch",
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
    },
]

product_create_invalid_data: list[dict[str, Any]] = [
    # Проверка создания продукта с отсутствующими
    # параметрами в конструкторе класса
    {
        "data_for_create": {
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000,
            "quantity": 23,
        },
        "exception_type": TypeError,
        "system_answer": "Product.__init__() missing 1"
        " required positional argument: 'name'",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "price": 57000,
            "quantity": 23,
        },
        "exception_type": TypeError,
        "system_answer": "Product.__init__() missing 1"
        " required positional argument: 'description'",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "description": "Лучшее устройство для лучшей связи",
            "quantity": 23,
        },
        "exception_type": TypeError,
        "system_answer": "Product.__init__() missing 1"
        " required positional argument: 'price'",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000,
        },
        "exception_type": TypeError,
        "system_answer": "Product.__init__() missing 1"
        " required positional argument: 'quantity'",
    },
]

product_create_invalid_data_type: list[dict[str, Any]] = [
    {
        "data_for_create": {
            "name": 1,
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": 1.1,
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": True,
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": [1, 2, 3],
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": (1, 2, 3),
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": {1, 2, 3},
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": {"prod": 1},
            "description": "Pro гейминг у тебя в кармане",
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "name должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1,
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1.1,
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": False,
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": [1, 2, 3],
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": {1, 2, 3},
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": (1, 2, 3),
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": {"prod": 1},
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1,
            "price": 32000.50,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "description должен быть str",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1.1,
            "price": "32000.50",
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": False,
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": [1, 2, 3],
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": {1, 2, 3},
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": (1, 2, 3),
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": {"prod": 1},
            "quantity": 16,
        },
        "exception_type": TypeError,
        "system_answer": "price должен быть числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1.1,
            "price": 37000,
            "quantity": "16",
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": 1.1,
            "price": 37000.50,
            "quantity": 16.2,
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": False,
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": [1, 2, 3],
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": {1, 2, 3},
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": (1, 2, 3),
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": {"prod": 1},
        },
        "exception_type": TypeError,
        "system_answer": "quantity должен быть int",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": -100,
            "quantity": 15,
        },
        "exception_type": ValueError,
        "system_answer": "price должно быть положительным числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 0,
            "quantity": 15,
        },
        "exception_type": ValueError,
        "system_answer": "price должно быть положительным числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": -2,
        },
        "exception_type": ValueError,
        "system_answer": "quantity должно быть положительным числом",
    },
    {
        "data_for_create": {
            "name": "Sony PSP 15",
            "description": "Развлечения всегда с тобой",
            "price": 37000,
            "quantity": 0,
        },
        "exception_type": ValueError,
        "system_answer": "quantity должно быть положительным числом",
    },
]

product_create_by_classmethod_invalid_data: list[dict[str, Any]] = [
    # Проверка создания продукта с отсутствующими
    # параметрами в конструкторе класса
    {
        "data_for_create": {
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000,
            "quantity": 23,
        },
        "exception_type": KeyError,
        "system_answer": "name",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "price": 57000,
            "quantity": 23,
        },
        "exception_type": KeyError,
        "system_answer": "description",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "description": "Лучшее устройство для лучшей связи",
            "quantity": 23,
        },
        "exception_type": KeyError,
        "system_answer": "price",
    },
    {
        "data_for_create": {
            "name": "IPhone 200",
            "description": "Лучшее устройство для лучшей связи",
            "price": 57000,
        },
        "exception_type": KeyError,
        "system_answer": "quantity",
    },
]

set_price_with_incorrect_type: list[dict[str, Any]] = [
    {"new_price": "1"},
    {"new_price": True},
    {"new_price": [1, 2, 3]},
    {"new_price": {1, 2, 3}},
    {"new_price": (1, 2, 3)},
    {"new_price": {"test_price": 1}},
]

add_incorrect_objects: list[dict[str, Any]] = [
    {
        "incorrect_object": 1,
        "expected_answer": "'int' object has no attribute 'price'",
    },
    {
        "incorrect_object": 1.1,
        "expected_answer": "'float' object has no attribute 'price'",
    },
    {
        "incorrect_object": "1",
        "expected_answer": "'str' object has no attribute 'price'",
    },
    {
        "incorrect_object": False,
        "expected_answer": "'bool' object has no attribute 'price'",
    },
    {
        "incorrect_object": [1, 2, 3],
        "expected_answer": "'list' object has no attribute 'price'",
    },
    {
        "incorrect_object": (1, 2, 3),
        "expected_answer": "'tuple' object has no attribute 'price'",
    },
    {
        "incorrect_object": {1, 2, 3},
        "expected_answer": "'set' object has no attribute 'price'",
    },
    {
        "incorrect_object": {"object": 1},
        "expected_answer": "'dict' object has no attribute 'price'",
    },
]
