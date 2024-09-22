from abc import ABC, abstractmethod


# Abstract class defining the structure or template for executing a recipe.
class AbstractRecipe(ABC):

    # Template method defines the steps to execute the recipe.
    # Subclasses will define the specifics of each step.
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    # Abstract methods that must be implemented by any subclass.
    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


# Subclass that implements the specific steps of the template.
class MicrowaveRecipe(AbstractRecipe):

    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')

    def recipe(self):
        print('execute the steps')

    def cleanup(self):
        print('switch off microwave')


# The Template Method pattern allows `execute` to follow the same sequence
# while subclasses like MicrowaveRecipe implement the details of each step.
MicrowaveRecipe().execute()
