from typing import Any

import pytest

from data_for_tests.smartphone_test_data.test_datasets import \
    category_create_invalid_data_type as invalid_types
from src.product import Smartphone
from src.tools.dataset_handlers import param_packer_old, value_packer_old


class TestSmartphoneCreation:

    @pytest.mark.smartphone_positive
    def test_smartphone_creation_by_init_method(
        self, create_smartphone: Smartphone
    ) -> None:
        assert create_smartphone.name == "Samsung Galaxy S23 Ultra"
        assert (
            create_smartphone.description == "256GB, Серый цвет, 200MP камера"
        )
        assert create_smartphone.price == 180000.0
        assert create_smartphone.quantity == 5
        assert create_smartphone.efficiency == 95.5
        assert create_smartphone.model == "S23 Ultra"
        assert create_smartphone.memory == 256
        assert create_smartphone.color == "Серый"

    @pytest.mark.smartphone_negative
    def test_smartphone_creation_without_efficiency(
        self, create_smartphone: Smartphone
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            Smartphone(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
                model="S23 Ultra",
                memory=256,
                color="Серый",
            )

        assert (
            "Smartphone.__init__() missing"
            " 1 required positional argument: 'efficiency'"
            == str(exc_info.value)
        )

    @pytest.mark.smartphone_negative
    def test_smartphone_creation_without_model(
        self, create_smartphone: Smartphone
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            Smartphone(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
                efficiency=95.5,
                memory=256,
                color="Серый",
            )

        assert (
            "Smartphone.__init__() missing"
            " 1 required positional argument: 'model'"
            == str(exc_info.value)
        )

    @pytest.mark.smartphone_negative
    def test_smartphone_creation_without_memory(
        self, create_smartphone: Smartphone
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            Smartphone(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
                efficiency=95.5,
                model="S23 Ultra",
                color="Серый",
            )

        assert (
            "Smartphone.__init__() missing"
            " 1 required positional argument: 'memory'"
            == str(exc_info.value)
        )

    @pytest.mark.smartphone_negative
    def test_smartphone_creation_without_color(
        self, create_smartphone: Smartphone
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            Smartphone(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
                efficiency=95.5,
                model="S23 Ultra",
                memory=256,
            )
        assert (
            "Smartphone.__init__() missing"
            " 1 required positional argument: 'color'"
            == str(exc_info.value)
        )

    @pytest.mark.smartphone_negative
    @pytest.mark.parametrize(
        param_packer_old(invalid_types), value_packer_old(invalid_types)
    )
    def test_smartphone_creation_with_incorrect_data_types(
        self,
        data_for_create: dict[str, Any],
        exception_type: type[Exception],
        system_answer: str,
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            Smartphone(**data_for_create)

            assert str(exc_info.value) == system_answer


class TestSmartphoneMethods:
    @pytest.mark.smartphone_positive
    def test_add_magic_method_call_positive(
        self, create_two_smartphone: tuple[Smartphone, Smartphone]
    ) -> None:
        smartphone1, smartphone2 = create_two_smartphone
        assert smartphone1 + smartphone2 == 2580000.0

    @pytest.mark.smartphone_negative
    def test_add_magic_method_call_negative(
        self, create_two_different_products: tuple
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            create_two_different_products[0] + create_two_different_products[1]

        assert (
            str(exc_info.value)
            == "объект 'LawnGrass' не является 'Smartphone'"
        )
