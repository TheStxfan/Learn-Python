from abc import ABC, abstractmethod
# prepare
# recipe
# cleanup


class AbstractRecipe(ABC):

    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


class MicrowaveRecipe1(AbstractRecipe):

    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')

    def recipe(self):
        print('execute the steps')

    def cleanup(self):
        print('switch off microwave')


MicrowaveRecipe1().execute()
