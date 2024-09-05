print("1. Hello World!\n")  # \n --> special character - new line

print("2. Hello " + "World!\n")  # + --> concatenation without space

print("3. Hello", "World!\n")  # , --> concatenation with space

print("4. Hello")
print("World!")  # prints on a new line

print("")  # --> print an empty string (leaves an empty line)
print()  # --> print an empty line (leaves an empty line)

print("5. Hello ", end="")  # end="" --> next print or input is on the same line
print("World!", end="\n")  # end="\n" --> next print or input is on the following line

print("6. test\n")

print("8. Hello", end=" World!")  # "end" specifies what is displayed at the end of the line
print(" test\n")                  # the next print or input will be on the same line.

print("10. Hello\"World")  # "\" is an escape character. It tells the code to not treat the next character as command
print('11. Hello"World')

print("12. Hello",
      end=" World!\n")  # this is another way of end=""

input()  # waits for any user input followed by the enter key before continuing
input("Enter your name: ")  # waits for user input (specific input) before continuing the program

input("This is a prompt.")  # the text displayed by an input command is called a prompt
