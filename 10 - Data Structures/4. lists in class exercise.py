class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"{name} is added to the students list.")

    def get_name_with_marks(self):
        print(f"{self.name}: {self.marks}")

    def get_number_of_marks(self):
        print(f"Number of marks: {len(self.marks)}")

    def get_total_sum_of_marks(self):
        print(f"Sum of marks: {sum(self.marks)}")

    def determine_maximum_mark(self):
        print(f"Maximum mark: {max(self.marks)}")

    def determine_minimum_mark(self):
        print(f"Minimum mark: {min(self.marks)}")

    def determine_average(self):
        if len(self.marks) > 0:
            print(f"Average: {sum(self.marks) / len(self.marks)}")
        else:
            print("No marks to calculate average.")

    def add_new_mark(self, mark):
        self.marks.append(mark)
        print(f"{mark} was added to the list of marks.")

    def remove_mark_at_index(self, index):
        if 0 <= index < len(self.marks):
            index_to_pop = self.marks[index]
            self.marks.pop(index)
            print(f"{index_to_pop} was removed from the list of marks.")
        else:
            print(f"The index {index} does not exist.")


new_student = Student("Adam", [1, 3, 5, 7])
print()
new_student.get_name_with_marks()
new_student.get_number_of_marks()
new_student.get_total_sum_of_marks()
new_student.determine_maximum_mark()
new_student.determine_minimum_mark()
new_student.determine_average()
print()
new_student.add_new_mark(0)
new_student.get_name_with_marks()
new_student.remove_mark_at_index(2)
new_student.get_name_with_marks()
