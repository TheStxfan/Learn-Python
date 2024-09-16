# It's true. Everything in Python is an object.

print(type(5))
print(type(True))
print(type("Hello"))
print(type(5.5))
print()

# Calling methods on objects
print("Hello".upper())  # HELLO
print()


def do_something(): pass


print(do_something)  # This displays the memory address of the function object
print(type(do_something))  # This displays the type of the function object, which is 'function'


# If you change the methods of an Object, it will change the memory address of the object
def do_something():
    print("something")

    return 3+3


print(do_something)
print(do_something())

test = do_something

print()
print(test)
print(type(test))
print(test())


