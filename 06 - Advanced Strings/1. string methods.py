# 1 - applying string methods
"hello world".upper()                                 # "HELLO WORLD"
"HELLO World".lower()                                 # "hello world"
"hello world".capitalize()                            # "Hello world"
"hello world".title()                                 # "Hello World"
"hELLO wORLD".swapcase()                              # "Hello World"
"hello world".center(18, "*")          # "****hello world****"
"hello world".ljust(18, "*")           # "hello world******"
"hello world".rjust(18, "*")           # "******hello world"

# 2 - formatting strings
"  hello  ".strip()                                   # "hello"
"  hello".lstrip()                                    # "hello"
"hello  ".rstrip()                                    # "hello"
"hello world".replace("world", "Python")  # "hello Python"
"hello world".split()                                 # ["hello", "world"]
", ".join(["apple", "banana", "cherry"])              # "apple, banana, cherry"
"Hello, {}".format("world")                           # "Hello, world"
"{} {}".format("Hello", "world")                # "Hello world"

# 3 - display strings with padding
"{:10}".format("test")                                # "test      " (in 10 spaces)
f"{'test':10}"
"{:^10}".format("test")                               # "   test   " (centered in 10 spaces)
f"{'test':^10}"
"{:>10}".format("test")                               # "      test" (right-aligned in 10 spaces)
f"{'test':>10}"
"{:<10}".format("test")                               # "test      " (left-aligned in 10 spaces)
f"{'test':<10}"

# 3.1 - display strings with custom padding
"{:+^10}".format("test")                              # "+++test+++" (centered with padding)
"{:*<10}".format("test")                              # "test******" (left-aligned with padding)
"{:->10}".format("test")                              # "------test" (right-aligned with padding)

# 4 - finding string methods
"hello world".count("l")                              # 3 --> counts the number of occurrences of a substring
len("hello world")                                    # 11 --> counts
var1 = "hello world"[0]                               # "h" --> indexing starts from 0
var2 = "hello world"[-1]                              # "d" --> negative indexing starts from the end
var3 = "hello world"[6:11]                            # "world" --> indexing from 6 to 11
var4 = "hello world"[6:]                              # "world" --> indexing from 6 to the end
var5 = "hello world"[:5]                              # "hello" --> indexing from the beginning to 5
var6 = "hello world"[:]                               # "hello world" --> indexing from the beginning to the end
var7 = "hello world"[::2]                             # "hlowrd" --> indexing with a step of 2
var8 = "hello world"[::-1]                            # "dlrow olleh" --> reversing the string

# 5 - finding the first occurrence of the substring
"hello world".find("world")                           # 6 --> (if not found, returns -1)
"hello world".rfind("world")                          # 6 --> (searches from the end)
"hello world".index("world")                          # 6 --> (if not found, Raises ValueError)
"hello world".rindex("world")                         # 6 --> (searches from the end, Raises ValueError)

# 6 - checking string type methods
"HELLO".isupper()                                     # True
"hello".islower()                                     # True
"   ".isspace()                                       # True
"abc".isalpha()                                       # True
"123".isdigit()                                       # True
"Hello World".istitle()                               # True
"1234".isnumeric()                                    # True
"hello world".startswith("hello")                     # True
"hello world".endswith("world")                       # True
"hello123".isalnum()                                  # True --> (only letters or|and numbers)
"hello world".isprintable()                           # True --> (only printable characters)
"hello\nworld".isprintable()                          # False
