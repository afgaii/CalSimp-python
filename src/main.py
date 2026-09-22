import logging
from logging_config import configure_log
from exceptions import CalculatorBaseError
from calculator import Calculator


def main():
    configure_log()  # Configure logging at the start of the program
    logger = logging.getLogger(__name__)
    calculator = Calculator()

    try:
        # print("add(5, 3) =", calculator.add(5, 3))
        # print("subtract(10, 4) =", calculator.subtract(10, 4))
        # print("multiply(6, 7) =", calculator.multiply(6, 7))
        # print("divide(8, 2) =", calculator.divide(8, 2))
        # print(
        #     "divide(8, 0) =", calculator.divide(8, 0)
        # )  # This will raise ZeroDivisionError
        # print("power(2, 3) =", calculator.power(2, 3))
        # print("modulus(10, 3) =", calculator.modulus(10, 3))
        # print(
        #     "modulus(10, 0) =", calculator.modulus(10, 0)
        # )  # This will raise ZeroDivisionError
        print("square_root(16) =", calculator.square_root(16))
        print(
            "square_root(-4) =", calculator.square_root(-4)
        )  # This will raise CalculatorBaseError
    except CalculatorBaseError as e:
        logger.error(f"Calculator error occurred: {e}")


if __name__ == "__main__":
    main()
