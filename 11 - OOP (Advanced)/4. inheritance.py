# Inheritance allows a subclass to inherit methods and attributes from a superclass.
# - Superclass: The class being inherited from.
# - Subclass: The class that inherits from the superclass and can add or override methods.

# Example 1: Independent classes

class Animal:
    def bark(self):
        print('bark')


animal = Animal()
animal.bark()  # Calls the bark method from Animal


# Class Pet, not inheriting from Animal

class Pet:
    def bark(self):
        print('bark')

    def groom(self):
        print('groom')


pet = Pet()
pet.bark()   # Calls the bark method from Pet
pet.groom()  # Calls the groom method from Pet


# Example 2: Subclassing
# Pet becomes a subclass of the superclass Animal. This means that it inherits its methods.

class Pet(Animal):
    def groom(self):
        print('groom')  # Adds a new method specific to Pet


pet = Pet()
pet.groom()  # Calls the groom method from Pet (subclass)
pet.bark()   # Inherits and calls the bark method from Animal (superclass)
