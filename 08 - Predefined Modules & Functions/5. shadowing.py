# Shadowing in Python occurs when a local variable or function has the same name as a global one, hiding the global
# version within its scope.

# Example:

# 'sum' is a built-in function used to sum all the numbers in an iterable.
numbers = [1, 3, 3, 54]
a = sum(numbers)
print(a)  # Output: 61

# Shadowing the 'sum' built-in function
sum = "Hello!"
print(sum)  # Displays the new value assigned to 'sum': "Hello!"

# Now I need to use the sum function again to sum some numbers.
numbers = [1, 3, 3, 54]
a = sum(numbers)  # This will cause an error, as 'sum' is now a string, not a function.
print(a)

