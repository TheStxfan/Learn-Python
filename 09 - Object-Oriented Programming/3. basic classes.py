# Creating a class
class Country:
    pass


# Creating objects of the Country() class
italy = Country()
usa = Country()
netherlands = Country()

# Creating attributes
italy.name = "Italy"
italy.capital = "Rome"

usa.name = "USA"
usa.capital = "Washington"

netherlands.name = "Netherlands"
netherlands.capital = "Amsterdam"

# Printing objects' state
print(italy.capital)     # Rome
print(netherlands.name)  # Netherlands

# In a class, each object has its own instances (attributes) of the data (state).


class MotorBike:
    pass


honda = MotorBike()
ducati = MotorBike()

honda.speed = 50
ducati.speed = 250

print(honda)
print(ducati)

print(honda.speed)
print(ducati.speed)

honda.speed = 150
print(honda.speed)
print(ducati.speed)
