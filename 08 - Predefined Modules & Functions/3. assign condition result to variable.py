# 1
number = 4
if number % 2 == 0:
    isEven = True
else:
    isEven = False

print(f"isEven = {isEven}")

# 2
number = 5
isEven = True if number % 2 == 0 else False

print(f"isEven = {isEven}")

# 3
isOdd = 3 % 2 != 0
print(f"isOdd  = {isOdd}")

# 4
isOdd = "Yes" if 2 % 2 != 0 else "No"
print(f"isOdd  = {isOdd}")
