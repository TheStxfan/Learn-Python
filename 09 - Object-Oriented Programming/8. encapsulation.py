# Encapsulation restricts access to a class's data and methods to protect data integrity.
# Example:

class MotorBike:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, amount):
        self.speed += amount

    """
    Encapsulation is important when actions should be controlled within certain limits.

    For example, the 'decrease_speed' method decreases the speed by the specified amount.
    Without encapsulation, directly modifying 'self.speed' could lead to unintended values, like a negative speed.
    By using methods to change speed, we can enforce rules (e.g., preventing speed from going below 0).
    """

    def decrease_speed(self, amount):
        if self.speed - amount >= 0:
            self.speed -= amount
        else:
            print("Speed cannot be negative.")


honda = MotorBike(50)
honda.decrease_speed(20)  # Reduces speed by 20, Output: 30

print(honda.speed)  # Output: 30

honda.decrease_speed(100)

print(honda.speed)  # Output: 30
