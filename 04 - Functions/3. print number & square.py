
def print_number(n):
    for i in range(1, n+1):
        print(i)


def print_squares_of_numbers(n):
    for i in range(1, n+1):
        print(f"{i} ^ 2 = {i**2}")


def call_all(n):
    print_number(n)
    print("\n")
    print_squares_of_numbers(n)


call_all(5)
