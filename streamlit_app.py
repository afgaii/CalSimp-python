import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

from calculator import Calculator
from exceptions import CalculatorBaseError
from logging_config import configure_log

configure_log()

st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("CalSimp: A Simple Calculator")

calculator = Calculator()

operation = st.selectbox(
    "Choose an operation:",
    [
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "modulus",
        "sqrt",
    ],
)

if operation == "sqrt":
    value = st.number_input("Number", value=0.0)

    if st.button("Calculate"):
        try:
            st.success(calculator.square_root(value))
        except CalculatorBaseError as e:
            st.error(e)

else:
    n1 = st.number_input("Number 1")
    n2 = st.number_input("Number 2")

    if st.button("Calculate"):
        try:
            result = calculator.operations(operation, n1, n2)
            st.success(result)
        except CalculatorBaseError as e:
            st.error(e)
