class Fan:
    def __init__(self, brand, radius, color):
        self.brand = brand
        self.radius = radius
        self.color = color
        self.is_on = False
        self.speed = False
        print(f"\nFan created: {brand}, {radius}, {color}\n")

    def switch_on(self, speed=0):
        if not self.speed == speed:
            self.speed = speed
            self.is_on = True
            print(f"\nFan is on. Speed set to: {self.speed}\n")
        else:
            print(f"\nSpeed is already set to: {self.speed}\n")

    def switch_off(self):
        self.speed = 0
        self.is_on = False
        print(f"\nFan is off.\n")

    def increase_speed(self):
        if self.speed == 0:
            self.switch_on(1)
        elif self.speed == 1:
            self.speed = 2
            print("\nSpeed increased to 2.\n")
        else:
            print("\nSpeed is at the maximum level.\n")

    def decrease_speed(self):
        if self.speed == 2:
            self.speed = 1
            print("\nSpeed decreased to 1.\n")
        elif self.speed == 1:
            self.switch_off()
        else:
            print("\nThe fan is currently off.\n")


input_name = input("New Fan Brand: ")
input_radius = input("Radius: ")
input_color = input("Color: ")

new_fan = Fan(input_name, input_radius, input_color)

menu = 0

while True:
    valid_choice_input = ("1", "2", "3")
    valid_speeds = ("1", "2")
    valid_increase_decrease = ("1", "2")

    if menu == 0:
        input_choice = input("1. Change the speed.\n2. Increase-Decrease\n3. Turn off.\n")
        if input_choice in valid_choice_input:
            if input_choice == "1":
                menu = 1
            elif input_choice == "2":
                menu = 2
            else:
                menu = 3
        else:
            print("Invalid choice.")

    elif menu == 1:
        input_speed = input("Set Speed to 1 or 2: ")
        if input_speed in valid_speeds:
            new_fan.switch_on(int(input_speed))
        else:
            print("Incorrect speed value.")
        menu = 0

    elif menu == 2:
        input_choice = input("1. Increase\n2. Decrease\n")
        if input_choice in valid_increase_decrease:
            if input_choice == "1":
                new_fan.increase_speed()
            else:
                new_fan.decrease_speed()
        menu = 0

    elif menu == 3:
        new_fan.switch_off()
        menu = 0
