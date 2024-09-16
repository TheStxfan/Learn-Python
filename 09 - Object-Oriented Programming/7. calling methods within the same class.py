class Planet:
    def __init__(self, name):
        self.name = name

    def rotate(self):
        print("Rotating")

    def revolve(self):
        print("Revolving")

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()


earth = Planet("Earth")

print(earth.name)

earth.rotate_and_revolve()
