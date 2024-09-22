# Run this code first without handling exceptions
# i = 0
# j = 10 / i    # This will raise a ZeroDivisionError
# print(j)      # Output: ZeroDivisionError: division by zero
# print('End')  # This line won't execute because of the error

# After running, comment lines 1 to 5 to continue with exception handling

# Now let's try to handle the exception with try and except. These commands are called constructs.

try:                    # Attempt to run this block
    i = 2
    j = 10 / i
    values = [1, '1']   # This will raise a TypeError as you can't sum int and string
    sum(values)
except:                 # Catch any exception that occurs and execute the next lines
    print('Exception')
    j = 0

print(j)      # Print the value of j after handling the exception
print('End')  # This will run now, as the exception is handled

input('\nPress Enter to continue.\n')

# You can also handle specific exceptions

try:
    i = 2
    j = 10 / i
    values = [1, '1']           # This will again raise a TypeError
    sum(values)
except TypeError:               # Handle TypeError (e.g., adding int and string)
    print('TypeError')
    j = 10                      # Default value for TypeError
except ZeroDivisionError:       # Handle division by zero error
    print('ZeroDivisionError')
    j = 0                       # Default value for ZeroDivisionError

print(j)      # This will print the value after the specific exception handling
print('End')

input('\nPress Enter to continue.\n')
# Multiple errors can be handled with the same code block

try:
    i = 2
    j = 10 / i
    values = [1, '1']
    sum(values)
except (TypeError, ZeroDivisionError):
    print('TypeError')
    j = 10
print('End')

input('\nPress Enter to continue.\n')
# Displaying more detailed error

try:
    sum([1, '1'])
except TypeError as error:
    print(error)  # unsupported operand type(s) for +: 'int' and 'str'
print('End')
