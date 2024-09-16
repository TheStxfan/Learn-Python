class Books:
    def __init__(self, name, copies=50):
        self.name = name
        self.copies = copies

    def increase_copies(self, amount=5):
        self.copies += amount

    def decrease_copies(self, amount=15):
        self.copies -= amount


The_12th_Planet = Books("The 12th Planet")                # 50
Dandelion_Wine = Books("Dandelion Wine", 25)              # 25
The_Martian_Chronicles = Books("The Martian Chronicles")  # 50

print(f"{The_12th_Planet.name}: {The_12th_Planet.copies}")
print(f"{Dandelion_Wine.name}: {Dandelion_Wine.copies}")
print(f"{The_Martian_Chronicles.name}: {The_Martian_Chronicles.copies}")
print()


The_12th_Planet.increase_copies()          # 55
Dandelion_Wine.decrease_copies(23)         # 2
The_Martian_Chronicles.increase_copies(2)  # 52

print(f"{The_12th_Planet.name}: {The_12th_Planet.copies}")
print(f"{Dandelion_Wine.name}: {Dandelion_Wine.copies}")
print(f"{The_Martian_Chronicles.name}: {The_Martian_Chronicles.copies}")
print()




