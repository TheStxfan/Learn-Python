import builtins

# The 'builtins' module provides direct access to all of Python's built-in functions, exceptions, and other objects.
# For example, 'builtins.len' refers to the built-in len() function.

# Normally, this module is implicitly available, so explicit import is not required.
# However, importing 'builtins' can be helpful when you override a built-in name (e.g., len, print)
# and still need access to the original built-in functionality.

# The most common exceptions hierarchy in Python:

# CLASSES
#     object
#         BaseException
#             BaseExceptionGroup
#                 ExceptionGroup(BaseExceptionGroup, Exception)
#             Exception
#                 ArithmeticError
#                     FloatingPointError
#                     OverflowError
#                     ZeroDivisionError
#                 AssertionError
#                 AttributeError
#                 BufferError
#                 EOFError
#                 ImportError
#                     ModuleNotFoundError
#                 LookupError
#                     IndexError
#                     KeyError
#                 MemoryError
#                 NameError
#                     UnboundLocalError
#                 OSError
#                     BlockingIOError
#                     ChildProcessError
#                     ConnectionError
#                         BrokenPipeError
#                         ConnectionAbortedError
#                         ConnectionRefusedError
#                         ConnectionResetError
#                     FileExistsError
#                     FileNotFoundError
#                     InterruptedError
#                     IsADirectoryError
#                     NotADirectoryError
#                     PermissionError
#                     ProcessLookupError
#                     TimeoutError
#                 ReferenceError
#                 RuntimeError
#                     NotImplementedError
#                     RecursionError
#                 StopAsyncIteration
#                 StopIteration
#                 SyntaxError
#                     IndentationError
#                         TabError
#                 SystemError
#                 TypeError
#                 ValueError
#                     UnicodeError
#                         UnicodeDecodeError
#                         UnicodeEncodeError
#                         UnicodeTranslateError
#                 Warning
#                     BytesWarning
#                     DeprecationWarning
#                     EncodingWarning
#                     FutureWarning
#                     ImportWarning
#                     PendingDeprecationWarning
#                     ResourceWarning
#                     RuntimeWarning
#                     SyntaxWarning
#                     UnicodeWarning
#                     UserWarning
#             GeneratorExit
#             KeyboardInterrupt
#             SystemExit
#         bytearray
#         bytes
#         classmethod
#         complex
#         dict
#         enumerate
#         filter
#         float
#         frozenset
#         int
#             bool
#         list
#         map
#         memoryview
#         property
#         range
#         reversed
#         set
#         slice
#         staticmethod
#         str
#         super
#         tuple
#         type
#         zip

# The following command will display detailed documentation on all built-in identifiers in Python.
# Running it in the Python console will give you a readable list of all built-in functions, exceptions, etc.
help(builtins)
