import builtins

# The 'builtins' module provides direct access to all of Python's built-in functions, exceptions, and other objects.
# For example, 'builtins.len' refers to the built-in len() function.

# Normally, this module is implicitly available, and you don't need to import it explicitly.
# However, importing 'builtins' can be helpful when you override a built-in name (e.g., len, print)
# and still need access to the original built-in functionality.

# The following command will display detailed documentation on all built-in identifiers in Python.
# Running it in the Python console will give you a readable list of all built-in functions, exceptions, etc.
help(builtins)
