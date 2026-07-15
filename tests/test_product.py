import pytest

from data_for_tests.product_test_data.test_datasets import \
    product_create_invalid_data as invalid_data
from data_for_tests.product_test_data.test_datasets import \
    product_create_invalid_data_type as data_type
from data_for_tests.product_test_data.test_datasets import \
    product_create_valid_data as valid_data
from src.product import Product
from src.tools.dataset_handlers import param_packer_old, value_packer_old


class TestProduct:

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
