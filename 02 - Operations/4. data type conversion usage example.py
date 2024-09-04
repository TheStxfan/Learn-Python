n = input("Enter a number between 1 and 9 to multiply by five: ")  # every user input is a string

print(n * 5)  # this is why this will print the string five times (concatenation)
print(n + n + n)  # this concatenates the string three times
print(n, n, n)  # this displays the string separately three times

n = int(n)    # this converts it into an integer

print(n * 5)  # this will print the number multiplied by five
