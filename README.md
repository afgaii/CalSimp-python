# CalSimp-python
Complete Python Calculator Project

## Steps

### 1. Create Github Repository and git clone it

```
git clone https://github.com/afgaii/CalSimp-python.git
```

### 2. Create virtual environment and install the required packeges

```
# create virtual env
python -m venv cal_venv

# activate the venv
.\cal_venv\Scripts\activate

# create requirements.txt
pip install -r requirements.txt
```


- `Push to github repository`
```bash
# add to staggig area
git add . 

# add local repository
git commit -m "two steps are done"

# add remote repository
git push -u origin main
```

### 3. Run all codes in `jupyter-notebook`
- We created `notebook/experiments.ipynb`
#### All Steps in notebooks:
1. Setup & Imports
2. Custom Exceptions
3. Logging Configuration
4. Create Calculator Class
5. Run Demo: for normal and error cases
6. Test with `pytest`

### 4. Create python files and move all codes from notebook
```
CalSimp-python/
│
├── notebooks/
│   |
|   └── experiments.ipynb
|
├── src/
│   |
|   └── __init__.py         # Tells Python that a folder is a package you can import from
│   |
|   └── calculator.py       # Add, divide, factorial, and other logic
│   |
|   └── exceptions.py       # Custom errors
│   |
|   └── logging_config.py   # Logging setup
│   |
|   └── main.py     # Run a short calculator demonstration
│
├── tests/
│   └── test_calculator.py  # Automated tests
│
└── logs/
|   └── calculator.log    # Saved log messages
|
|__ pyproject.toml        # Main configuration file
```
- To run python file
`python src\main.py`

- To run pytest
`python -m pytest`


`pyproject.toml` is the main configuration file for a modern Python project.
It tells Python tools important project information, such as:
- Project name and version
- Required Python version
- Dependencies, such as streamlit and pytest
- How to build/install the project
- Test settings
- Formatter and linter settings
