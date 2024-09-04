vowels = ("A", "E", "I", "O", "U")

letter = input("\nEnter here a letter: ").upper()

if letter.isalpha():
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("You have not entered a letter.")
