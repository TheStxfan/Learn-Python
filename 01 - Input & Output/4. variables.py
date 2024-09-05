# Assigning values to variables on different lines
apples = 10
oranges = 20
print(apples, oranges)  # printing the variables


# Assigning values to variables on the same line
apples, oranges = 15, 25
print(apples, oranges)


# Assigning the same value to variables on the same line
number_of_apples = number_of_oranges = 5
print(number_of_apples, number_of_oranges)


input("Press \"Enter\" to continue.")  # waiting for user input


# user input can be assigned to a variable
name = input("Enter your name: ")
print("Hello", name)

print("Enter your age:", end=" ")
age = input()
