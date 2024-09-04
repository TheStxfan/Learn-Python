
def check_is_prime(number):
    if number == 1:
        return "Not Prime"
    elif number == 2:
        return "Prime"

    if not isinstance(number, int):
        return "Not Prime"

    for i in range(2, number):
        if number % i == 0:
            return "Not Prime"

    return "Prime"


print()
print(check_is_prime(2))    # Prime
print(check_is_prime(3))    # Prime
print(check_is_prime(13))   # Prime
print(check_is_prime(29))   # Prime
print(check_is_prime(97))   # Prime
print()
print(check_is_prime(1))    # Not Prime
print(check_is_prime(4))    # Not Prime
print(check_is_prime(9))    # Not Prime
print(check_is_prime(25))   # Not Prime
print(check_is_prime(100))  # Not Prime
