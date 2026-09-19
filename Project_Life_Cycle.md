# Calculator Project: Complete lifecycle

```
1. Plan
   ├── Understand user needs
   ├── Functional requirements
   ├── Non-functional requirements
   ├── User stories
   └── Acceptance criteria
   ↓
2. Design
   ├── UI design
   ├── System design
   └── Database/API decisions
   ↓
3. Build
   ↓
4. Test
   ↓
5. Deploy
   ↓
6. Maintain and improve

```

### 1. **Plan**
- PM explains what users need.
- Example: “Users need a calculator that can add, subtract, multiply, and divide.”
- for calculator
```
| Type | Meaning | Example |
|---|---|---|
| Functional requirement | What the app must do | “The user can divide two numbers.” |
| Functional requirement | What the app must do | “The app shows an error for division by zero.” |
| Non-functional requirement | How well it must work | “The result appears in under one second.” |
| Non-functional requirement | Quality/security rule | “The app must not crash on invalid input.” |
| User story | User-focused requirement | “As a user, I want to calculate percentages.” |
| Acceptance criteria | How to prove it works | “When I enter 25 and 200, it shows 12.5%.” |
```
### 2. **Design**
- Decide how it should work and look.
- Example:
   - Python for calculations
   - Streamlit for the web page
   - Custom errors for invalid input
   - Logging for problems


#### MVP architecture

```text
User's browser
      |
      v
Streamlit interface
  - inputs
  - buttons
  - result/error display
      |
      v
Calculator service/class
  - validation
  - operations
  - custom exceptions
      |
      +-------------------> Application logs
      |                       - INFO: successful events
      |                       - ERROR: failures
      v
Result or controlled error
      |
      v
Streamlit displays response to user
```

How it works:
1. The user opens the Streamlit calculator in a browser.
2. The user chooses an operation, such as Add or Divide, and enters numbers.
3. Streamlit sends the operation and numbers to the Calculator class.
4. The Calculator class checks the input.
   - If it is valid, it calculates the answer.
   - If it is invalid, such as dividing by zero, it raises a custom error.
5. The calculator writes a log message.
   - INFO for a successful calculation.
   - ERROR for an invalid calculation.
6. Streamlit receives the result or error.
   - It shows the result, such as 5.0.
   - Or it shows a friendly message, such as Cannot divide by zero.

- Main files:
```
CalSimp-python/
│
├── notebooks/
│   |
|   └── calsimp_notebook.ipynb
|
├── src/
│   |
|   └── calculator.py         # Add, divide, factorial, and other logic
│   |
|   └── exceptions.py         # Custom errors
│   |
|   └── logging_config.py     # Logging setup
|   |
|   └── streamlit_app.py      # Web page: inputs, buttons, results
│
├── tests/
│   └── test_calculator.py  # Automated tests
│
└── logs/
    └── calculator.log    # Saved log messages
```

The important idea is separation:
- streamlit_app.py handles what the user sees.
- calculator.py handles maths and validation.
- exceptions.py handles known errors.
- logging_config.py decides where logs go.
- tests/ checks the app works correctly.

### 3. **Build**
- Write the code.
- Example:
    - calculator.py for calculation methods
    - exceptions.py for custom errors
    - streamlit_app.py for the user interface

### 4. **Test**
- Check normal and error cases.
- Example:
```
    assert calculator.add(2, 3) == 5
    with pytest.raises(DivisionByZeroError):
        calculator.divide(1, 0)
```
### 5. **Deploy**
- Make the application available to users.
- Example: publish the Streamlit app online.

### 6. **Maintain and improve**
- Fix bugs, check logs, listen to user feedback, and add useful features.
- Example: add calculation history after users request it.
```
PM request
   ↓
Requirements
   ├── Functional
   └── Non-functional
   ↓
User stories + acceptance criteria
   ↓
System design
   ↓
Development and testing
```