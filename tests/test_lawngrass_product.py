from typing import Any

import pytest

from data_for_tests.lawngrass_test_data.test_datasets import \
    lawngrass_create_invalid_data_type as invalid_types
from src.product import LawnGrass
from src.tools.dataset_handlers import param_packer_old, value_packer_old


class TestLawnGrassCreation:

    @pytest.mark.lawngrass_positive
    def test_lawngrass_creation_by_init_method(
        self, create_lawngrass: LawnGrass
    ) -> None:
        assert create_lawngrass.name == "Газонная трава"
        assert create_lawngrass.description == "Элитная трава для газона"
        assert create_lawngrass.price == 500.0
        assert create_lawngrass.quantity == 20
        assert create_lawngrass.country == "Россия"
        assert create_lawngrass.germination_period == "7 дней"
        assert create_lawngrass.color == "Зеленый"

    @pytest.mark.lawngrass_negative
    def test_lawngrass_creation_without_country(
        self, create_lawngrass: LawnGrass
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            LawnGrass(
                name="Газонная трава",
                description="Элитная трава для газона",
                price=500.0,
                quantity=20,
                germination_period="7 дней",
                color="Зеленый",
            )

        assert (
            "LawnGrass.__init__() missing 1"
            " required positional argument: 'country'"
            == str(exc_info.value)
        )

    @pytest.mark.lawngrass_negative
    def test_lawngrass_creation_without_germination_period(
        self, create_lawngrass: LawnGrass
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            LawnGrass(
                name="Газонная трава",
                description="Элитная трава для газона",
                price=500.0,
                quantity=20,
                country="Россия",
                color="Зеленый",
            )

        assert (
            "LawnGrass.__init__() missing 1"
            " required positional argument: 'germination_period'"
            == str(exc_info.value)
        )

    @pytest.mark.lawngrass_negative
    def test_lawngrass_creation_without_color(
        self, create_lawngrass: LawnGrass
    ) -> None:
        with pytest.raises(TypeError) as exc_info:
            LawnGrass(
                name="Газонная трава",
                description="Элитная трава для газона",
                price=500.0,
                quantity=20,
                country="Россия",
                germination_period="7 дней",
            )

        assert (
            "LawnGrass.__init__() missing"
            " 1 required positional argument: 'color'"
            == str(exc_info.value)
        )

    @pytest.mark.lawngrass_negative
    @pytest.mark.parametrize(
        param_packer_old(invalid_types), value_packer_old(invalid_types)
    )
    def test_lawngrass_creation_with_incorrect_data_types(
        self,
        data_for_create: dict[str, Any],
        exception_type: type[Exception],
        system_answer: str,
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            LawnGrass(**data_for_create)

            assert str(exc_info.value) == system_answer

class TestObjectMixin:

    def test_mixin_with_lawngrass(self,
                                  capsys):
        LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        )

        captured_output = capsys.readouterr()

        assert captured_output.out == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n'