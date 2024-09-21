from abc import ABC, abstractmethod


# An abstract class is a blueprint for other classes. It can't be instantiated directly.
# It allows you to define methods that must be implemented by any subclass.
class AbstractAnimal(ABC):
    # Abstract method: subclasses must provide an implementation for this method.
    @abstractmethod
    def bark(self):
        pass  # No implementation here, subclasses must define this behavior.


# Dog is a subclass of AbstractAnimal.
# It must implement the bark method as required by the abstract class.
class Dog(AbstractAnimal):
    def bark(self):
        print('Bow Bow')  # Provides specific implementation for the abstract bark method.


# Abstract classes enforce a contract.
# You should use them to ensure all subclasses implement required methods.
print(Dog().bark())  # Outputs: Bow Bow
