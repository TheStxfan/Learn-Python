"""
In Python, a tuple is an immutable, ordered collection of elements defined using parentheses ().
Once created, the elements in a tuple cannot be changed, added, or removed.
Tuples are useful for storing related data that should remain constant.
"""


def create_country():
    return 'Italy', 'Rome', 20  # Returns a tuple with three elements: name, capital, and number of regions.


# Storing the values returned by the function in a variable (tuple)
country = create_country()
print(type(country))  # Output: <class 'tuple'>

name, capital, regions = country  # Unpacking/Destructing the tuple into individual variables
print(name, capital, regions)
print(country[0], country[1], country[2])
print(len(country))

"""
Creating a tuple with a single element requires a trailing comma (,).
Otherwise, it will be treated as a string or a number.
A tuple can be created without parentheses, but their usage is usually preferred for readability.
"""

x = (1)   # x = 1 would do the same
y = (1,)  # x = 1, would do the same
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'tuple'>

