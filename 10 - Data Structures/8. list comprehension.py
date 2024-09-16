numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# List Comprehension
example_list = [number for number in numbers]
print(example_list)

example_list = [len(number) for number in numbers]
print(example_list)

example_list = [number.upper() for number in numbers]
print(example_list)


# 1
numbers_length_four = []

for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)

print(numbers_length_four)

# Same logic but with list comprehension
numbers_length_five = [number for number in numbers if len(number) == 5]

print(numbers_length_five)


# 2
numbers = [3, 6, 9, 1, 4, 15, 6, 3]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
print(even_numbers)
print(odd_numbers)
