from string import punctuation

main_string = "This is an awesome occasion. This has never happened before."

letters_count = {}
words_count = {}
punctuation_count = {}

# letters_count
for letter in main_string:
    letters_count[letter] = letters_count.get(letter, 0) + 1

print(letters_count)

# words_count
words = main_string.split(" ")  # extracting the words from the list
words = [word.strip(punctuation) for word in words]  # removing punctuation from the words in the list

for word in words:
    words_count[word] = words_count.get(word, 0) + 1

print(words_count)

# punctuation_count
for char in main_string:
    if char in punctuation:
        punctuation_count[char] = punctuation_count.get(char, 0) + 1

print(punctuation_count)
