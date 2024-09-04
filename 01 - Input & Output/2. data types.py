
# to check the type of data
type(45)                # <class 'int'>    --> integer
type("Hello, World!")   # <class 'str'>    --> string
type(3.14)              # <class 'float'>  --> float
type(True)              # <class 'bool'>   --> boolean

# you can also convert data types with the following commands
int(45)                   # convert to integer
str("Test")                 # convert to string
float(4.5)                # convert to float
bool(True)                # convert to boolean

# convertion example
int(3.5)                  # 3
float(4)                  # 4.0
str(5)                    # "5"
bool(1)                   # True
int(False)                # 0

# display the type of data
print(type("variable_or_value_to_check"))

# check if data is of a specific type
isinstance(3, int)        # True
isinstance("Hello", str)  # True
isinstance(7.5, float)    # True
isinstance(False, bool)   # True

