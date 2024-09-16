marks = [45, 54, 80, 43, 10]
fruits = ["apple", "banana"]
float_list = [1.1, 2.2]


# 1. Adding elements to a list
print("1. Adding elements to a list")
marks.append(99)                            # Adds 99 at the end
print(marks)

marks = marks + [3, 4]                      # Adds two integers at the end of the list
print(marks)

marks += [5, 6]                             # Adds two integers at the end of the list
print(marks)

marks.insert(2, 100)         # Inserts 100 at index 2
print(marks)

int_extend_list = []
int_extend_list.extend([60, 70])            # Extends the list by adding multiple elements
print(int_extend_list)

animals_extend_list = []
animals_extend_list.extend("fish")          # Extends animals_extend_list with each character of the string "fish"
print(animals_extend_list)

animals_extend_list.extend(["cat", "dog"])  # Extends animals_extend_list with two string elements
print(animals_extend_list)

# 2. Adding elements of different types to a list
print("\n2. Adding elements of different types to a list")
fruits.append("cherry")                    # Adds "cherry" at the end
print(fruits)

float_list.insert(1, 3.3)   # Inserts 3.3 at index 1
print(float_list)

# 3. Removing elements from a list
print("\n3. Removing elements from a list")
marks.pop()                # Removes the last element
print(marks)

marks.pop(2)               # Removes the element at index 2
print(marks)

del marks[4]               # Removes the element at index 4
print(marks)

marks.remove(80)           # Removes the first occurrence of 80
print(marks)

fruits.remove("banana")    # Removes "banana" from the fruits list
print(fruits)

# 4. Retrieving data from a list
print("\n4. Retrieving data from a list")
print(marks[2])            # Retrieves the element at index 2
print(marks.index(54))     # Finds the index of 54
print(45 in marks)         # Checks if 45 is in the list
print(45 not in marks)     # Checks if 45 is not in the list
print(marks.count(45))     # Counts the occurrences of 45

# 5. Changing the order of elements in a list
print("\n5. Changing the order of elements in a list")

marks.sort()                  # Sorts the list in ascending order
print(marks)

fruits.sort()                 # Strings are sorted in alphabetical order
print(fruits)

marks.reverse()               # Reverses the list order
print(marks)

# 6. Clearing a list
print("\n6. Clearing a list")
marks.clear()                 # Clears all elements
print(marks)

# 7. Looping through a list of different types
print("\n7. Looping through a list of different types")
for fruit in fruits:
    print(fruit, end=" ")

# 8. Slicing a list
print("\n\n8. Slicing a list")
indexes = [0, 1, 2, 3, 4, 5, 6]

"""
--> Tips to remember easier:
 - [start:stop:step]
 - Start : included
 - Stop  : excluded
 - Step  : step
 - [:]   = Elements divisor. Think of it as "from -> to"
 
--> Example:
 - marks[-1:-4:-1]  # [70, 60, 99]
 
 > Breakdown
 - [-1] = Start : included
 - [-4] = Stop  : excluded
 - [-1] = Step 
 
--> Example 2:
 - marks[:3]  # [45, 54, 80]
 
 > Breakdown
 - The start is not specified, so it defaults to the beginning of the list.
 - [3] = Stop - excluded
 - No step specified, so it defaults to 1.
 
--> Example 3:
 - marks[1:6:2]  # [54, 43, 60]

 > Breakdown
 - [1] = Start : included
 - [6] = Stop  : excluded
 - [2] = Step
"""

print(indexes[1:4])                     # [1, 2, 3]             : Retrieves elements from index 1 to 3
print(indexes[:3])                      # [0, 1, 2]             : Retrieves elements from the start to index 2
print(indexes[3:])                      # [3, 4, 5, 6]          : Retrieves elements from index 3 to the end
print(indexes[-3:])                     # [4, 5, 6]             : Retrieves the last three elements
print(indexes[:-2])                     # [0, 1, 2, 3, 4]       : Retrieves all elements except the last two
print(indexes[::2])                     # [0, 2, 4, 6]          : Retrieves every second element
print(indexes[::3])                     # [0, 3, 6]             : Retrieves every third element
print(indexes[::-1])                    # [6, 5, 4, 3, 2, 1, 0] : Retrieves elements in reverse order
print(indexes[::-3])                    # [6, 3, 0]             : Retrieves every third element in reverse order
print(indexes[1:6:2])                   # [1, 3, 5]             : Retrieves every second element from index 1 to 5
print(indexes[-1:-4:-1])                # [6, 5, 4]             : Retrieves elements in reverse from the end
print()

# Removing elements with slicing
indexes = [0, 1, 2, 3, 4, 5, 6]
del indexes[3:]                         # Deleting elements from index 3 to the end
print(indexes)                          # [0, 1, 2]

indexes = [0, 1, 2, 3, 4, 5, 6]
del indexes[2:5]                        # Deleting elements from index 2 to 5 (excluded)
print(indexes)                          # [0, 1, 5, 6]

indexes = [0, 1, 2, 3, 4, 5, 6]
indexes[1:4] = ["one", "two", "three"]  # Replacing elements from index 1 to 4 with strings
print(indexes)                          # [0, "one", "two", "three", 4, 5, 6]
