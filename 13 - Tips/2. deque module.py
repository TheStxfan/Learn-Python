from collections import deque

# deque is an efficient way to implement a stack/queue in Python.
# It's more optimal than using a list for adding/removing elements at both ends.

queue = deque(['Zero', 'One', 'Two'])

queue.pop()                    # Removes and returns the last element.
print(queue)

queue.popleft()                # Removes and returns the first element.
print(queue)

queue.append('Three')          # Adds an element to the end.
print(queue)

queue.appendleft('Minus One')  # Adds an element to the beginning.
print(queue)
