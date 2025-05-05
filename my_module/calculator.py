# my_module/calculator.py
def add(x, y):
    """Adds two numbers together."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Inputs must be numbers")
    return x + y

def subtract(x, y):
     """Subtracts y from x."""
     # Intentionally introduce a potential pylint warning (missing docstring)
     # and maybe a flake8 issue (e.g., extra space)
     return x -  y