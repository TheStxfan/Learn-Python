def example_method(mandatory_parameter, default_parameter='Default', *args, **kwargs):
    print(f'mandatory_parameter = {mandatory_parameter}')
    print(f'default_parameter = {default_parameter}')
    print(f'args = {args}')  # Prints additional positional arguments (*args) as a tuple.
    print(f'kwargs = {kwargs}')  # Prints additional named arguments (*kwargs) as a dictionary.
    print()


example_method(1, 2, 3, 4, 5, 6)

# The following commands unpack a variable containing lists with args or kwargs in a method.
example_list = [1, 2, 3, 4, 5, 6]
example_method(*example_list)  # All the values from example_list get passed as arguments to the example_method.

example_dict = dict(a='1', b='2')
example_method(*example_list, **example_dict)
