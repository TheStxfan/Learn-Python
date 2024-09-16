components = ["mouse", "monitor", "pc", "case", "keyboard", "usb", "button"]

# Not modifying the original list
for component in sorted(components):    # Prints the elements sorted without sorting the list
    print(component)
print()

for component in reversed(components):  # Prints the elements in reversed order without reversing the list order
    print(component)
print()

# Keys
for component in sorted(components, key=len):  # Prints sorted elements based on their length
    print(component)
print()

for component in sorted(components, key=len, reverse=True):  # Prints sorted elements based on their reversed length
    print(component)
print()

# Sorting the list
components.sort(key=len)
print(components)

components.sort(key=len, reverse=True)
print(components)











