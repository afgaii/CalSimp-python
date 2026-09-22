import math
import logging
from exceptions import CalculatorBaseError, ZeroDivisionError

logger = logging.getLogger(__name__)


class Calculator:
    """Provides basic arithmetic operations.
    Operations include addition, subtraction, multiplication, division, power, modulus, and square root.
    """

    # we can use this dictionary to map operation names to method names
    OPERATIONS = {
        "add": "add",
        "subtract": "subtract",
        "multiply": "multiply",
        "divide": "divide",
        "power": "power",
        "modulus": "modulus",
        "square_root": "square_root",
    }

    def add(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        result = a + b
        logger.info(f"Adding {a} and {b}: Result = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of a and b."""
        result = a - b
        logger.info(f"Subtracting {b} from {a}: Result = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of a and b."""
        result = a * b
        logger.info(f"Multiplying {a} and {b}: Result = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Returns the quotient of a and b. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            logging.error("Attempted to divide by zero.")
            raise ZeroDivisionError("Cannot divide by zero.")

        result = a / b
        logger.info(f"Dividing {a} by {b}: Result = {result}")
        return result

    def power(self, a: float, b: float) -> float:
        """Returns a raised to the power of b."""
        result = a**b
        logger.info(f"Raising {a} to the power of {b}: Result = {result}")
        return result

    def modulus(self, a: float, b: float) -> float:
        """Returns the modulus of a and b."""
        if b == 0:
            logging.error("Attempted to compute modulus with divisor zero.")
            raise ZeroDivisionError("Cannot compute modulus with divisor zero.")
        result = a % b
        logger.info(f"Computing modulus of {a} and {b}: Result = {result}")
        return result

    def square_root(self, a: float) -> float:
        """Returns the square root of a. Raises CalculatorBaseError if a is negative."""
        if a < 0:
            logging.error("Attempted to compute square root of a negative number.")
            raise CalculatorBaseError(
                "Cannot compute square root of a negative number."
            )

        result = math.sqrt(a)
        logger.info(f"Computing square root of {a}: Result = {result}")
        return result

    def operations(self, operation: str, *args) -> float:
        """Performs the specified operation with the given arguments."""
        method_name = self.OPERATIONS.get(operation)

        if method_name is None:
            logging.error(
                f"Invalid operation '{operation}' requested."
            )  # ("Invalid operation %s", operation)
            raise CalculatorBaseError(
                f"Invalid operation '{operation}'. Supported operations are: {list(self.OPERATIONS.keys())}"
            )

        # method name is "add" => self.add(*args)
        method = getattr(self, method_name)  # self.add
        result = method(*args)
        logger.info(
            f"Performed operation '{operation}' with arguments {args}: Result = {result}"
        )
        return result
