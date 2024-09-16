"""
A dictionary in Python is a mutable, unordered collection of unique key-value pairs
"""

occurrences = dict(a=5, b=6, c=8)

print(occurrences)

# Adding a new key-value pair
occurrences['d'] = 9
print(occurrences)

# Modifying a value
occurrences['a'] = 10
print(occurrences)

# Accessing values in a dictionary
print(occurrences['a'])  # Prints the value associated with the key 'a'. If the key doesn't exist, it raises a KeyError.
print(occurrences.get('b'))  # If the key exists, returns its value. Else, returns None.
print(occurrences.get('x'))  # If the key doesn't exist, it returns None.
print(occurrences.get('z', 404))  # If the key doesn't exist, returns 404. Else, returns its value.

# Checking if a key exists
print('a' in occurrences)  # Prints True if the key 'a' exists in the dictionary, False otherwise.

# Removing a key-value pair
del occurrences['a']

# Printing existing things
print(occurrences.keys())    # Prints a list of all keys in the dictionary.
print(occurrences.values())  # Prints a list of all values in the dictionary.
print(occurrences.items())   # Prints all pairs in the dictionary as tuples (key, value). More on tuples later.

# Iterating over a dictionary
for key, value in occurrences.items():
    print(f"{key} {value}")
