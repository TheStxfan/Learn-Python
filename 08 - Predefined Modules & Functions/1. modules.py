# Modules are files containing Python code that define functions, classes, variables, or executable code.
# They help organize and reuse code across projects and are preferable to creating an entire program in a single file.
# Python includes several built-in modules that can be imported directly without additional installation.
# Common built-in modules include 'string', 'os', 'sys', 'math', etc.
# Additionally, you can download and install external modules using pip.
# Popular external modules include 'requests', 'pandas', 'numpy', 'matplotlib', etc.
# Install external modules with 'pip install module_name'
# This command must be executed in a terminal, not inside a Python console.

# To use a module, use the 'import' statement:
# import module_name  # Imports the entire module

# To import specific functions or classes from a module, use 'from ... import ...':
# from module_name import function_name  # Imports only the specified function or class
# Although less common, you can import all functions or classes from a module with 'from ... import *'

# To import a module with a shorter alias, use 'import ... as ...':
# import module_name as alias  # Imports the module with the alias 'alias'

# Example usage:
# import math       # Imports the entire math module
# math.sqrt(4)      # Uses the module to calculate the square root of 4

# from math import sqrt  # Imports only the sqrt function from math
# sqrt(4)                # Uses the sqrt function directly

# import math as m  # Imports the math module with the alias 'm'
# m.sqrt(4)         # Calls the sqrt function using the alias 'm'
