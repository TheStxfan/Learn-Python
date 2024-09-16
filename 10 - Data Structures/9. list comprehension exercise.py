from string import punctuation

words = "Hello, World!".split(" ")  # ['Hello,', 'World!']

words = [word.strip(punctuation) for word in words]

print(words)
