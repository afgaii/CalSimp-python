from calculator import Calculator
from exceptions import CalculatorBaseError, ZeroDivisionError
import pytest


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


# calculator = Calculator()  # Create a single instance of Calculator for all tests


def test_basic_operations(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(4, 2) == 8
    assert calculator.divide(10, 2) == 5.0
    assert calculator.power(2, 3) == 8
    assert calculator.modulus(10, 3) == 1
    assert calculator.square_root(16) == 4
    assert calculator.operations("add", 5, 3) == 8


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


def test_modulus_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.modulus(10, 0)


def test_square_root_of_negative(calculator):
    with pytest.raises(CalculatorBaseError):
        calculator.square_root(-4)


def test_invalid_operation(calculator):
    with pytest.raises(CalculatorBaseError):
        calculator.operations("invalid_op", 5, 3)
