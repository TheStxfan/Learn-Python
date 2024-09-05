# 1
print("\n" + "-" * 40)
print("\n1 - What will this display?\n")
print('for i in range(1, 11, 2):\n    print(i, end=" ")')
input("\nAnswer:")

for i in range(1, 11, 2):
    print(i, end=" ")

input('\n\nPress "Enter" to continue.')

# 2
print("\n" + "-" * 40)
print("\n2 - What will this display?\n")
print('for i in range(11, 1, -1):\n    print(i, end=" ")')
input("\nAnswer:")

for i in range(11, 1, -1):
    print(i, end=" ")

input('\n\nPress "Enter" to continue.')

# 3
print("\n" + "-" * 40)
print("\n3 - What will this display?\n")
print('for i in range(11, 0, -1):\n    print(i, end=" ")')
input("\nAnswer:")

for i in range(11, 0, -1):
    print(i, end=" ")

input('\n\nPress "Enter" to continue.')

# 4
print("\n" + "-" * 40)
print("\n4 - What will this display?\n")
print('''i = 5
while i*i < 10:
    print(i)
print("Done")''')
input("\nAnswer:")

i = 5
while i*i < 10:
    print(i)
print("Done")

input('\nPress "Enter" to continue.')

# 5
print("\n" + "-" * 40)
print("\n5 - What will this display?\n")
print('''i = 2
while i*i < 10:
    print(i, end=" ")
    i = i + 1
print("Done")''')
input("\nAnswer:")

i = 2
while i*i < 10:
    print(i, end=" ")
    i = i + 1
print("Done")

input('\nPress "Enter" to continue.')

# 6
print("\n" + "-" * 40)
print("\n6 - What will this display?\n")
print('''for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print("Done")''')
input("\nAnswer:")

for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print("Done")

input('\nPress "Enter" to continue.')

# 7
print("\n" + "-" * 40)
print("\n7 - What will this display?\n")
print('''for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i, end=" ")
print("Done")''')
input("\nAnswer:")

for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i, end=" ")
print("Done")

input('\nPress "Enter" to continue.')

# 8
print("\n" + "-" * 40)
print("\n8 - What will this display?\n")
print('''for i in range(1, 11):
    if i % 2:         
        continue      
    print(i, end=" ") 
print("Done")''')
print("\nFor this one, you can check the explanation from line 112.")
input("\nAnswer:")

for i in range(1, 11):
    if i % 2:          # If i is odd
        continue       # Skips the current iteration
    print(i, end=" ")  # Prints only even numbers
print("Done")

input('\nPress "Enter" to continue.')

# 9
print("\n" + "-" * 40)
print("\n9 - What will this display?\n")
print('''for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print("Done")''')
input("\nAnswer:")

for i in range(1, 11):
    if i % 2 != 0:
        continue  # Skips odd numbers
    print(i, end=" ")  # Prints only even numbers
print("Done")

input('\nPress "Enter" to continue.')
