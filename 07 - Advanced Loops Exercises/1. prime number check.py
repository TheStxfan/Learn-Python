# Prime number: divisible only by 1 and itself

def check_is_prime(number):

    prime = True
    if not isinstance(number, int) or number < 2:
        prime = False

    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        return f"Prime: {number}."
    else:
        return f"Not Prime: {number}."


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
