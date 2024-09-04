print("Hello World!\n")  # \n --> special character - new line

print("Hello " + "World!\n")  # + --> concatenation without space

print("Hello", "World!\n")  # , --> concatenation with space

print("Hello")
print("World!")  # prints on a new line

print("")  # --> print an empty string (leaves an empty line)
print()  # --> print an empty line (leaves an empty line)

print("Hello ", end="")  # end="" --> next print or input is on the same line
print("World!", end="\n")  # end="\n" --> next print or input is on the following line
print("test\n")

print("Hello", end=" World!")  # end displays " World!" at the end of the line; next print or input is on the same line
print(" test\n")

print("Hello",
      end=" World!\n")  # this is another way of end=""

input()  # waits for any user input followed by the enter key before continuing
input("Enter your name: ")  # waits for user input (specific input) before continuing the program

input("This is a prompt.")  # the text displayed by an input command is called a prompt
