import string
import os  # this new module provides a way to interact with the operating system


def clear_terminal():
    os.system('cls')  # using the os module to clear the terminal (doesn't work in IDE's terminal)


vowels = ("A", "E", "I", "O", "U")  # define vowels

"""
First way of retrieving all the capital alphabet letters (easier)
"""

alphabet = string.ascii_uppercase  # get uppercase alphabet
letters = []  # initialize letters list

for letter in alphabet:  # for letter in alphabet
    letters.append(letter)  # add the letter as separate item at the end of the letters list

print()
print("First Method:")
print(alphabet)
print(letters)


"""
Second way of retrieving all the capital alphabet letters (the more complex one, exercise)
"""

alphabet = string.ascii_letters  # get alphabet
letters = []  # initialize letters list

for letter in alphabet:  # for letter in alphabet
    if letter.isupper():  # if the letter is uppercase
        letters.append(letter)  # add the letter as separate item at the end of the letters list

print()
print("Second Method:")
print(alphabet)
print(letters)
input()


# starting user actions
while True:

    user_input = input("\nEnter here a letter: ")  # get user input
    letter = user_input.upper()  # convert it to uppercase

    if letter in letters:  # if the user input is in the letters list
        if letter in vowels:  # if it is in the vowels list
            print(f"{letter} is a vowel.")  # the letter is a vowel
        else:  # else
            print(f"{letter} is a consonant.")  # the letter is a consonant
        break  # break out of the loop (runs inside the if statement)

    else:  # if the user input is not in the letters list
        print("You have not entered a letter.")  # no detected letter
        input("Press Enter to try again.\n")  # display try again and pause so that user can read the message
        clear_terminal()  # clearing the terminal
