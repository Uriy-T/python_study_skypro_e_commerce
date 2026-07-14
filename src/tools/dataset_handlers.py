from typing import Any


def value_packer(data: list[dict]) -> list[tuple]:
    """
    Анализирует входную структуру данных и формирует список параметров
    для тестирования в pytest.fixture(params=...)
    :param data: входящий список словарей для анализа
    :return: список кортежей содержащих перечисление значений
    для тестирования объекта.
    """
    main_data_set = [list(item.values())[0] for item in data]
    return [tuple(item.values()) for item in main_data_set]


def param_packer(data: list[dict[str, Any]]) -> str:
    """
    Анализирует входную структуру данных и формирует список параметров
    для тестирования в pytest.mark.parametrize().
    :param data: входящий список словарей для анализа.
    :return: строка с перечислением параметров для тестирования
    объекта.
    """
    main_data_set = [list(item.values())[0] for item in data][0]
    return ', '.join(main_data_set.keys())


def param_packer_old(data: list[dict[str, Any]]) -> str:
    """
    Анализирует входную структуру данных и формирует список параметров
    для тестирования в pytest.mark.parametrize().
    :param data: входящий список словарей для анализа.
    :return: строка с перечислением параметров для тестирования
    объекта.
    """
    return ", ".join(list(data[0].keys()))


def value_packer_old(data: list[dict[str, Any]]) -> list[tuple]:
    """
    Анализирует входную структуру данных и формирует список наборов
    значений для тестирования в pytest.mark.parametrize().
    :param data: входящий список словарей для анализа.
    :return: список кортежей содержащих перечисление значений
    для тестирования объекта.
    """
    return [tuple(item.values()) for item in data]
