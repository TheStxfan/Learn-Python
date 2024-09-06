# Object-Oriented Programming (OOP)
# Thinking about Objects

"""
 - Class:
    1. Member Data/State/Fields
    2. Actions/Methods/Behaviour
    3. Objects/Instances
"""

# Procedural/Structured Programming
# Thinking in Terms of Procedures/Methods/Functions

# A procedural function outlines sequential steps for a task, using global data accessible throughout the program.
# A procedural function like fly() defines a sequence of steps for a task, where each step is globally accessible.

"""
// Global Data

fly() {
    travelToAirport();
    findCheckInCounter();
    checkIn();
    passSecurityCheck();
    waitForBoardingCall();
    boardTheFlight();
    wishTheAirHostess();
    takeOff();
    haveFun();
    landing();
}
"""

# Object-Oriented Programming Examples

# Flight Objects
"""
Airplane
    - Data: airline, make, type, position
    - Actions: takeOff(), land(), cruise()

AirHostess
    - Data: name, address
    - Actions: wish(), serve()

Passenger
    - Data: name, address
    - Actions: takeCab(), checkIn(), wait(), smile()
"""

# Online Shopping System
"""
Customer
    name, address
    login(), logout(), selectProduct(product)

Shopping Cart
    items
    add(item), remove(item)

Product
    name, price, quantityAvailable
    order(), changePrice()
"""

# Person
"""
Person
    name, address, hobbies, work
    walk(), run(), sleep(), eat(), drink()
"""

# Object-Oriented Programming - Classes
# A class in OOP is a blueprint for creating objects, defining their data (attributes) and behaviors (methods).

"""
class Planet:  # Class
    # Data/State/Fields
    name = ""
    location = ""
    distance_from_sun = 0.0

    # Actions/Behavior/Methods
    def revolve(self):
        pass

    def rotate(self):
        pass

# Objects/Instances
earth = Planet()  
venus = Planet()
"""