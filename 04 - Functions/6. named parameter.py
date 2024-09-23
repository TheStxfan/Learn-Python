def print_string(string="Hello, World!", n=2):
    # Print the given string n times.
    for i in range(1, n + 1):
        print(string)


# Default usage
print_string()
print("\n")

# Custom string
print_string("Not default")
print("\n")

# Custom string with specified repetitions
print_string("Not default", 4)
print("\n")

# Using a named parameter for clarity
print_string(n=4)  # Here, "n=4" is a named parameter.
