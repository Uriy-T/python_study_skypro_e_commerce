from typing import Any

import pytest

from data_for_tests.category_test_data.test_datasets import \
    add_product_incorrect_type as incorrect_product
from data_for_tests.category_test_data.test_datasets import \
    category_create_invalid_data as c_invalid_data
from data_for_tests.category_test_data.test_datasets import \
    category_create_invalid_data_type as c_invalid_data_type
from data_for_tests.category_test_data.test_datasets import \
    category_create_valid_data as c_valid_data
from src.category import Category
from src.product import Product
from src.tools.dataset_handlers import param_packer_old, value_packer_old


class TestCategory:

    @pytest.mark.category_positive
    def test_create_category_positive(
        self,
        create_category: Category,
    ) -> None:
        assert (
            create_category.name == c_valid_data[0]["expected_values"]["name"]
        )
        assert (
            create_category.description
            == c_valid_data[0]["expected_values"]["description"]
        )
        assert isinstance(create_category.get_products, list)
        assert (
            create_category.product_count
            == c_valid_data[0]["expected_values"]["product_count"]
        )
        assert (
            create_category.category_count
            == c_valid_data[0]["expected_values"]["category_count"]
        )

    @pytest.mark.category_positive
    def test_create_category_logic(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )

        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )

        category1 = Category(
            name="Игровые консоли",
            description="Игровые консоли, геймпады, аксессуары, расширения",
            products=[product1, product2],
        )

        assert Category.category_count == 2
        assert category1.product_count == 2

        product3 = Product(
            "Canon 600 XT", "Камера + базовый объектив", 75000.00, 6
        )

        category2 = Category(
            name="Фототехника",
            description="Камеры, фоны, освещение",
            products=[product3],
        )

        assert Category.category_count == 3

    # Негативные тесты создания категории
    @pytest.mark.category_negative
    def test_create_category_without_name(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Category(
                description=c_invalid_data[0]["data_for_create"][
                    "description"
                ],
                products=c_invalid_data[0]["data_for_create"]["products"],
            )

        assert c_invalid_data[0]["system_answer"] in str(exc_info.value)

    @pytest.mark.category_negative
    def test_create_category_without_description(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Category(
                name=c_invalid_data[1]["data_for_create"]["name"],
                products=c_invalid_data[1]["data_for_create"]["products"],
            )

        assert c_invalid_data[1]["system_answer"] in str(exc_info.value)

    @pytest.mark.category_negative
    def test_create_category_without_products(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Category(
                name=c_invalid_data[2]["data_for_create"]["name"],
                description=c_invalid_data[2]["data_for_create"][
                    "description"
                ],
            )

            assert c_invalid_data[2]["system_answer"] in str(exc_info.value)

    @pytest.mark.category_negative
    @pytest.mark.parametrize(
        param_packer_old(c_invalid_data_type),
        value_packer_old(c_invalid_data_type),
    )
    def test_create_category_with_incorrect_data_types(
        self,
        data_for_create: dict,
        exception_type: type[Exception],
        system_answer: str,
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            Category(*data_for_create.values())

            assert str(exc_info.value) == system_answer


class TestGetProducts:

    @pytest.mark.category_positive
    def test_get_products(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )

        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )

        category = Category(
            name="Игровые консоли",
            description="Игровые консоли, геймпады, аксессуары, расширения",
            products=[product1, product2],
        )

        products = category.get_products
        assert isinstance(products, list)
        assert len(products) == 2
        for elem in products:
            assert isinstance(elem, str)


class TestAddProduct:

    # Позитивные тесты добавления продукта
    @pytest.mark.category_positive
    def test_add_new_product(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )
        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )
        category = Category(
            name="Игровые консоли",
            description="Игровые консоли, геймпады, аксессуары, расширения",
            products=[product1],
        )
        assert len(category.get_products) == 1
        assert (
            category.get_products[0] == "Xbox series X, 56000.0 руб."
            " Остаток: 30"
        )

        category.add_product(product2)
        assert len(category.get_products) == 2
        assert (
            category.get_products[1] == 'NES "reborn", 4500.5 руб.'
            " Остаток: 11"
        )

    @pytest.mark.category_positive
    def test_add_exist_product_more_price(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )
        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )
        product3 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 100000.00, 12
        )
        category = Category(
            name="Игровые консоли",
            description="Игровые консоли, геймпады, аксессуары, расширения",
            products=[product1, product2],
        )

        category.add_product(product3)

        category.add_product(product2)
        assert len(category.get_products) == 2
        assert (
            category.get_products[0] == "Xbox series X, 100000.0 руб."
            " Остаток: 42"
        )

    @pytest.mark.category_positive
    def test_add_exist_product_less_price(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )
        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )
        product3 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 40000.00, 26
        )
        category = Category(
            name="Игровые консоли",
            description="Игровые консоли, геймпады, аксессуары, расширения",
            products=[product1, product2],
        )

        category.add_product(product3)

        category.add_product(product2)
        assert len(category.get_products) == 2
        assert (
            category.get_products[0] == "Xbox series X, 56000.0 руб."
            " Остаток: 56"
        )

    # Негативные тесты добавления продукта
    @pytest.mark.category_negative
    @pytest.mark.parametrize(
        param_packer_old(incorrect_product),
        value_packer_old(incorrect_product),
    )
    def test_add_product_incorrect_type(
        self, create_category: Category, add_product: Any
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            create_category.add_product(add_product)

            assert (
                str(exc_info.value) == "add_product должен быть типом Product"
            )
