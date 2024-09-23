# A Python module is a script containing functions and classes for use in other files.
# Module names cannot start with a number or contain spaces; they must start with a letter or an underscore.
# It's advisable to avoid naming methods with a leading underscore.

def method_1(color):
    print(f'method {color}')


class ClassA:
    def class_method_1(self, material):
        print(f'class method 1: {material}')


# When a module is imported, any top-level code (not within functions or classes) is executed.
# Functions and classes are defined but not executed until called.
method_1('Transparent')
ClassA().class_method_1('Glass')
print()

# The following block runs only if the script is executed directly, not when imported.
if __name__ == '__main__':
    method_1('Brown')
    ClassA().class_method_1('Wood')
