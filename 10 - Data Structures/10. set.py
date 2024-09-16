numbers = [45, 45, 80, 80]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

# Adding to a set an existing element
numbers_set.add(80)
print(numbers_set)

# Adding to a set a non-existing element
numbers_set.add(55)
print(numbers_set)

# Removing from a set
numbers_set.remove(45)
print(numbers_set)

"""
Sets they don't allow duplicates.
Sets are mutable, but the their elements must be immutable.
Sets are unordered, so they do not support indexing.
Sets do not support concatenation.
"""

# numbers_set[0]  # As sets do not support indexing, this would result in an error.

# You can check if a value is present in a set
print(80 in numbers_set)  # True
print(90 in numbers_set)  # False

"""
Sets support iteration.
Sets support built-in functions like len(), max(), min(), and sum().
"""

# You can create a set using range()
first_set = set(range(1, 6))
print(numbers_set)  # {1, 2, 3, 4, 5}

second_set = set(range(4, 11))
print(second_set)   # {4, 5, 6, 7, 8, 9, 10}

# "first_set + second_set" will result in an error, as sets do not support concatenation.
# To combine two sets, you can use the "union()" method or the "|" operator.

first_combined_set = first_set | second_set
print(first_combined_set)              # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

second_combined_set = first_set.union(second_set)
print(second_combined_set)             # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# To find the intersection of two sets, you can use the intersection() method or the & operator.
first_intersection_set = first_set & second_set
print(first_intersection_set)          # {4, 5}

second_intersection_set = first_set.intersection(second_set)
print(second_intersection_set)         # {4, 5}

# Subtraction of sets
first_subtraction_set = first_set - second_set  # elements present in first_set but not in second_set
print(first_subtraction_set)            # {1, 2, 3}

first_subtraction_set = second_set - first_set
print(first_subtraction_set)            # {6, 7, 8, 9, 10}
