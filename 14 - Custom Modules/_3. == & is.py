"""
In Python "==" (Equality operator): Checks if the values of two objects are equal.
It compares the actual data stored in the objects.
On the other hand, "is" (Identity operator): Checks if two variables refer to the same object in memory.
It compares the identity of the objects, not their values.
"""

list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
list3 = list1               # list3 points to the same object as list1

print(list1 == list2)       # True: list1 and list2 have the same content (values).
print(list1 is list2)       # False: list1 and list2 are different objects in memory.

print()
print(list1 == list3)       # True: list1 and list3 have the same content.
print(list1 is list3)       # True: list1 and list3 point to the same object in memory.

print()
print(id(list1))            # id() shows the memory address of the object.
print(id(list2))
print(id(list3))
print()


# However Note:
class Student:
    def __init__(self, number):
        self.number = number


student1 = Student(1)
student2 = Student(2)
student3 = Student(1)
student4 = student1

print(student1 is student2)  # False
print(student1 is student3)  # False
print(student1 is student4)  # True

# Classes equality cannot be compared with "==". They can be compared with the "__eq__" method.
print(student1 == student3)  # False


# Example
class Student:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number


student1 = Student(1)
student2 = Student(2)
student3 = Student(1)
student4 = student1

print(student1 == student2)  # False
print(student1 == student3)  # True
print(student1 == student4)  # True
