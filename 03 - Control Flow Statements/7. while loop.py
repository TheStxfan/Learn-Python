counter = 0

while counter < 3:
    counter += 1
    print("Counter:", counter)

print("\nExited while loop.\n")


input('''The following loop is an infinite loop.
The only way to stop it is by closing the program,
stopping it if in an IDE, or by pressing "Ctrl + C" 
if running in a terminal.

Press enter to start the loop.''')

# this loop will also display how many times it runs
i = 0
while True:
    i += 1
    print(f"{i} Infinite loop.")
