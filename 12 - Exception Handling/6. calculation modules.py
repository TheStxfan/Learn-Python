from decimal import Decimal
import math
import statistics

# Float is not fully precise for decimal arithmetic in Python.
print('1.', 4.5 - 3.2)   # 1.2999999999999998

# For higher precision, use the Decimal module.
value1 = Decimal('4.5')  # Decimal accepts numeric strings for accurate calculations.
value2 = Decimal('3.2')
print('2.', value1 - value2)  # 1.3

# The math module offers basic to complex mathematical operations.
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print()

# Common math functions:
# gcd(), factorial(), sin(), cos(), tan(), log(), log10(), degrees(), radians(), ceil()

# View all available functions in the math module:
# help(math)

# To display documentation for a specific function:
print(help(math.gcd))
print()
print(help(math.factorial))
print()

# The statistics module provides functions for statistical calculations.
marks = [1, 2, 3, 4, 4, 5]
print(statistics.mean(marks))           # Mean: 3.1666666666666665
print(statistics.median(marks))         # Median: 3.5
print(statistics.mode(marks))           # Mode: 4
print(statistics.median_low(marks))     # Median low: 3
print(statistics.median_high(marks))    # Median high: 4
print(statistics.variance(marks))       # Variance: 2.1666666666666665
