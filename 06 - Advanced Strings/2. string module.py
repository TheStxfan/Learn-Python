# To display available modules with TAB, install pyreadline3 with the following command in CMD
# python -m pip install pyreadline3
# # Modules will be explained in more detail in section 08.

from string import *

test = "a"

var1 = ascii_letters    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
var2 = ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
var3 = ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var4 = digits           # '0123456789'
var5 = hexdigits        # '0123456789abcdefABCDEF'
var6 = octdigits        # '01234567'
var7 = punctuation      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
var8 = printable        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
var9 = whitespace       # ' \t\n\r\x0b\x0c'

print(test in var1)
print(test in var2)
print(test in var3)
print(test in var4)
print(test in var5)
print(test in var6)
print(test in var7)
print(test in var8)
print(test in var9)
