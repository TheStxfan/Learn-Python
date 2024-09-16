"""
 - Queue = First in first out (FIFO)
 - Stack = Last in first out (LIFO)
"""

# Queue
print("Queue:")
numbers = [0, 1, 2, 3, 4, 5, 6]

while len(numbers) > 0:
    print(numbers.pop(0))

print()

# Stack
print("Stack:")
numbers = [0, 1, 2, 3, 4, 5, 6]

while len(numbers) > 0:
    print(numbers.pop())
