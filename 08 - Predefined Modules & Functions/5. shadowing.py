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

# Skip to line 18 for now
# del sum

# Now I need to use the sum function again to sum some numbers.
numbers = [1, 3, 3, 54]
a = sum(numbers)  # This will cause an error, as 'sum' is now a string, not a function.
print(a)

# Try running the code now.
# The message displayed is: TypeError: 'str' object is not callable
# There are two ways to avoid this issue:
# 1. Rename the local variable (the one that shadows the built-in function), for example, 'sum_'.
# 2. Use 'del sum' to delete the local variable 'sum' so that only the built-in function can be executed.
# You can now go back to line 16, uncomment the 'del sum' line and run the code again.
