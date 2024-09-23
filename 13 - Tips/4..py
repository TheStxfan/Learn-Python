def example_method(mandatory_parameter, default_parameter='Default',
                   *args, **kwargs):
    print(f"""mandatory_parameter = {mandatory_parameter}
default_parameter = {default_parameter}
args = {args}
kwargs = {kwargs}
""")


example_method(25)
example_method(25, 'Some String')
example_method(25, 'String 1', 'String 2', 'String 3')
example_method(25, 'String 1', 'String 2', 'String 3', key1='a', key2='b')
example_method(25, 'String 1', key1='a', key2='b')










