class CalculatorBaseError(Exception):  # Base class is inherited from Exception class
    """Base class for exceptions in this module."""

    pass


class ZeroDivisionError(
    CalculatorBaseError
):  # ZeroDivisionError class is inherited from CalculatorBaseError class
    """Exception raised when attempting to divide by zero."""

    pass
