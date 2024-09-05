# basic function
def print_hello_world():    # defining the function
    print("Hello, World!")


print_hello_world()         # calling the function


# Functions in Python can return any type of value, from basic data types, to functions and objects (explained later)
def print_hello_world():
    return "Hello, World!"


print(print_hello_world())


# functions return "None" if no return value is specified
def print_hello_world():
    var = "this variable is not used"


print(print_hello_world())
