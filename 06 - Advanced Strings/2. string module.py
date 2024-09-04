# To display available modules with TAB, install pyreadline3 with the following command in CMD
# python -m pip install pyreadline3

import string

test = "a"

var1 = string.ascii_letters    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
var2 = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
var3 = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var4 = string.digits           # '0123456789'
var5 = string.hexdigits        # '0123456789abcdefABCDEF'
var6 = string.octdigits        # '01234567'
var7 = string.punctuation      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
var8 = string.printable        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
var9 = string.whitespace       # ' \t\n\r\x0b\x0c'

print(test in var1)
print(test in var2)
print(test in var3)
print(test in var4)
print(test in var5)
print(test in var6)
print(test in var7)
print(test in var8)
print(test in var9)
