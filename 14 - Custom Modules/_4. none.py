"""
In Python, None represents the absence of a value or a null value.
- Example usage:
-> A function that does not return a value explicitly returns None.
-> A variable that has no value assigned.
-> Default values for function parameters when no other value is provided.
-> Signals the end of lists or loops.
"""

print(type(None))  # <class 'NoneType'>


def email(subject, content, to, cc=None, bcc=None):    # Setting default values as empty.
    print(f'{subject}, {content}, {to}, {cc}, {bcc}')


email('subject', 'great work', 'example@gmail.com')
email('None', 'great work', 'example@gmail.com')


var = None
if var is None: print('Do something.')
