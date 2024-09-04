
def print_string(string="Hello, World!", n=2):
    for i in range(1, n + 1):
        print(string)


print_string()
print("\n")
print_string("Not default")
print("\n")
print_string("Not default", 4)
print("\n")
print_string(n=4)

# in "print_string(n=4)", "n=4" is called "named parameter"
