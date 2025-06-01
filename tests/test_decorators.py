from typing import Any

import pytest

from src.decorators import log


@log(filename=None)
def my_function(x: Any, y: Any) -> Any:
    """Тестовая функция с декоратором"""
    return x / y


def test_decorator_log() -> Any:
    """Тестирование декоратора без выхода ошибки"""

    def my_function_(x: Any, y: Any) -> Any:
        return x / y

    assert my_function_(6, 3) == 2


def test_decorator_log_error() -> None:
    """Тестирование декоратора с выходом ошибки"""
    with pytest.raises(Exception):
        my_function(6, 0)


def test_decorator_cupsys_error(capsys: Any) -> Any:
    """Тестирование декоратора с выходом ошибки с 'cupsys'"""
    with pytest.raises(Exception):
        my_function(9, 0)
        captured = capsys.readouterr()
        assert "error" in captured.out


def test_decorator_cupsys_positive(capsys: Any) -> Any:
    """Тестирование декоратора с выходом ошибки с 'cupsys'"""
    with pytest.raises(Exception):
        my_function(6, 3)
        captured = capsys.readouterr()
        assert "error" in captured.out
