def example_method(mandatory_parameter, default_parameter='Default', *args, **kwargs):
    
    print(f'mandatory_parameter = {mandatory_parameter}')
    print(f'default_parameter = {default_parameter}')
    print(f'args = {args}')      # Prints additional positional arguments (*args) as a tuple.
    print(f'kwargs = {kwargs}')  # Prints additional named arguments (*kwargs) as a dictionary.
    print()


# Examples of calling the function with different arguments
example_method(25)  # Only mandatory parameter
example_method(25, 'Some String')  # Mandatory and default parameters
example_method(25, 'String 1', 'String 2', 'String 3')  # Including args
example_method(25, 'String 1', 'String 2', 'String 3', key1='a', key2='b')  # Including args and kwargs
example_method(25, 'String 1', key1='a', key2='b')  # Mixing positional and named kwargs
