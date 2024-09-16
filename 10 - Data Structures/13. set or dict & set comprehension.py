"""
In Python, there are two different ways to create a set:
1. Using the set() function: Converts an iterable (like a list) into a set, automatically removing duplicates.
2. Using {} with set comprehension: Creates a set directly. Note that {} is also used for creating dictionaries.

Note: Using empty curly braces "{}" creates a dictionary by default, not a set.
"""


is_a_set = {1, 2}  # Creates a set when values are provided without key-value pairs.
is_a_dictionary = {1: 1, 2: 2}  # Creates a dictionary when key-value pairs are provided.
print(is_a_set)
print(type(is_a_set))

# Example list
squares_first_ten_numbers = [number ** 2 for number in range(1, 11)]
print(squares_first_ten_numbers)

# Creating a set containing the same elements as squares_first_ten_numbers
squares_to_set_1 = set(squares_first_ten_numbers)            # First way: using the set() function
squares_to_set_2 = {number ** 2 for number in range(1, 11)}  # Second way: using set comprehension
print(squares_to_set_1)
print(squares_to_set_2)

# Creating a set containing the same elements as squares_first_ten_numbers
squares_to_dict = {number: number ** 2 for number in range(1, 11)}
print(squares_to_dict)
