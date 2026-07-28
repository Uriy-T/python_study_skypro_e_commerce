from typing import Any
from unittest.mock import Mock, patch

import pytest
from pytest import CaptureFixture

from data_for_tests.product_test_data.test_datasets import \
    add_incorrect_objects
from data_for_tests.product_test_data.test_datasets import \
    product_create_by_classmethod_invalid_data as cm_invalid_data
from data_for_tests.product_test_data.test_datasets import \
    product_create_invalid_data as invalid_data
from data_for_tests.product_test_data.test_datasets import \
    product_create_invalid_data_type as data_type
from data_for_tests.product_test_data.test_datasets import \
    product_create_valid_data as valid_data
from data_for_tests.product_test_data.test_datasets import \
    set_price_with_incorrect_type as incorrect_price
from src.product import Product
from src.tools.dataset_handlers import param_packer_old, value_packer_old


class TestProductCreation:

    # Позитивные тесты создания продукта

    @pytest.mark.product_positive
    def test_create_product_positive(
        self, create_product_valid: Product
    ) -> None:
        assert (
            create_product_valid.name
            == valid_data[0]["expected_values"]["name"]
        )
        assert (
            create_product_valid.description
            == valid_data[0]["expected_values"]["description"]
        )
        assert (
            create_product_valid.price
            == valid_data[0]["expected_values"]["price"]
        )
        assert (
            create_product_valid.quantity
            == valid_data[0]["expected_values"]["quantity"]
        )

    @pytest.mark.product_positive
    def test_create_product_by_classmethod(
        self, create_product_by_classmethod: Product
    ) -> None:
        assert (
            create_product_by_classmethod.name
            == valid_data[0]["expected_values"]["name"]
        )
        assert (
            create_product_by_classmethod.description
            == valid_data[0]["expected_values"]["description"]
        )
        assert (
            create_product_by_classmethod.price
            == valid_data[0]["expected_values"]["price"]
        )
        assert (
            create_product_by_classmethod.quantity
            == valid_data[0]["expected_values"]["quantity"]
        )

    # Негативные тесты создания через конструктор класса
    @pytest.mark.product_negative
    def test_create_product_without_name(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Product(
                description=invalid_data[0]["data_for_create"]["description"],
                price=invalid_data[0]["data_for_create"]["price"],
                quantity=invalid_data[0]["data_for_create"]["quantity"],
            )

        assert invalid_data[0]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_without_description(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Product(
                name=invalid_data[1]["data_for_create"]["name"],
                price=invalid_data[1]["data_for_create"]["price"],
                quantity=invalid_data[1]["data_for_create"]["quantity"],
            )

        assert invalid_data[1]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_without_price(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Product(
                name=invalid_data[2]["data_for_create"]["name"],
                description=invalid_data[2]["data_for_create"]["description"],
                quantity=invalid_data[2]["data_for_create"]["quantity"],
            )

        assert invalid_data[2]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_without_quantity(self) -> None:
        with pytest.raises(TypeError) as exc_info:
            Product(
                name=invalid_data[3]["data_for_create"]["name"],
                description=invalid_data[3]["data_for_create"]["description"],
                price=invalid_data[3]["data_for_create"]["price"],
            )

        assert invalid_data[3]["system_answer"] in str(exc_info.value)

    # Негативные тесты создания через метод класса
    @pytest.mark.product_negative
    def test_create_product_by_classmethod_without_name(self) -> None:
        with pytest.raises(KeyError) as exc_info:
            Product.new_product(cm_invalid_data[0]["data_for_create"])

        assert cm_invalid_data[0]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_by_classmethod_without_without_description(
        self,
    ) -> None:
        with pytest.raises(KeyError) as exc_info:
            Product.new_product(cm_invalid_data[1]["data_for_create"])

        assert cm_invalid_data[1]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_by_classmethod_without_without_price(self) -> None:
        with pytest.raises(KeyError) as exc_info:
            Product.new_product(cm_invalid_data[2]["data_for_create"])

        assert cm_invalid_data[2]["system_answer"] in str(exc_info.value)

    @pytest.mark.product_negative
    def test_create_product_by_classmethod_without_without_quantity(
        self,
    ) -> None:
        with pytest.raises(KeyError) as exc_info:
            Product.new_product(cm_invalid_data[3]["data_for_create"])

        assert cm_invalid_data[3]["system_answer"] in str(exc_info.value)

    # Негативные тесты создания объекта класса с неверными типами данных
    @pytest.mark.product_negative
    @pytest.mark.parametrize(
        param_packer_old(data_type), value_packer_old(data_type)
    )
    def test_create_product_with_incorrect_types(
        self,
        data_for_create: dict,
        exception_type: type[Exception],
        system_answer: str,
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            Product(*data_for_create.values())

            assert str(exc_info.value) == system_answer


class TestSetProductPrice:

    # Позитивные тесты логики изменения параметра price
    @pytest.mark.product_positive
    def test_set_price_more_than_actual(
        self, create_product_valid: Product
    ) -> None:
        assert (
            create_product_valid.price
            == valid_data[0]["expected_values"]["price"]
        )

        create_product_valid.price = 100000

        assert create_product_valid.price == 100000

    @pytest.mark.product_positive
    @patch("builtins.input", return_value="y")
    def test_set_price_less_than_actual_apply(
        self, mock_input: Mock, create_product_valid: Product
    ) -> None:
        assert (
            create_product_valid.price
            == valid_data[0]["expected_values"]["price"]
        )

        create_product_valid.price = 10000
        assert create_product_valid.price == 10000
        mock_input.assert_called_once()

    @pytest.mark.product_positive
    @patch("builtins.input", return_value="n")
    def test_set_price_less_than_actual_decline(
        self, mock_input: Mock, create_product_valid: Product
    ) -> None:
        assert (
            create_product_valid.price
            == valid_data[0]["expected_values"]["price"]
        )

        create_product_valid.price = 10000
        assert create_product_valid.price == 57000
        mock_input.assert_called_once()

    # Негативные тесты метода изменения параметра price
    # Установка отрицательного и нулевого значения параметра price

    @pytest.mark.product_negative
    def test_set_zero_price(
        self, capsys: CaptureFixture, create_product_valid: Product
    ) -> None:
        create_product_valid.price = 0
        captured_message = capsys.readouterr()
        assert (
            captured_message.out == "Product(Samsung Galaxy S 200,"
            " Лучшее устройство для лучшей связи, 57000.0, 23)\n"
            "Цена не должна быть нулевая или отрицательная\n"
        )

    @pytest.mark.product_negative
    def test_set_negative_price(
        self, capsys: CaptureFixture, create_product_valid: Product
    ) -> None:
        create_product_valid.price = -100
        captured_message = capsys.readouterr()
        assert (
            captured_message.out == "Product(Samsung Galaxy S 200,"
            " Лучшее устройство для лучшей связи, 57000.0, 23)\n"
            "Цена не должна быть нулевая или отрицательная\n"
        )

    # Установка невалидных типов для значения параметра price

    @pytest.mark.product_negative
    @pytest.mark.parametrize(
        param_packer_old(incorrect_price), value_packer_old(incorrect_price)
    )
    def test_set_price_with_incorrect_data_type(
        self, create_product_valid: Product, new_price: Any
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            create_product_valid.price = new_price

        assert str(exc_info.value) == "new_price должен быть числом"


class TestMagicMethod:

    @pytest.mark.product_positive
    def test_str_method(self, create_product_valid: Product) -> None:
        assert (
            create_product_valid.__str__()
            == "Samsung Galaxy S 200, 57000.0 руб. Остаток: 23 шт."
        )

    @pytest.mark.product_positive
    def test_add_method(self) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )

        product2 = Product(
            'NES "reborn"', "Консоль, 2 геймпада, 5000 игр", 4500.50, 11
        )

        assert product1 + product2 == 1729505.5

    @pytest.mark.product_negative
    @pytest.mark.parametrize(
        param_packer_old(add_incorrect_objects),
        value_packer_old(add_incorrect_objects),
    )
    def test_add_method_incorrect_object(
        self, incorrect_object: Any, expected_answer: str
    ) -> None:
        product1 = Product(
            "Xbox series X", "Консоль + 2 геймпада", 56000.00, 30
        )

        with pytest.raises(TypeError) as exc_info:
            product1 + incorrect_object

        assert str(exc_info.value) == expected_answer


class TestObjectMixin:

    def test_mixin_with_product(self, capsys: CaptureFixture) -> None:
        Product(
            name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=5,
        )

        captured_output = capsys.readouterr()

        assert (
            captured_output.out == "Product(Samsung Galaxy S23 Ultra,"
            " 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n"
        )
