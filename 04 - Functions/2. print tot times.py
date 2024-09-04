
def print_hello_world(n):
    for i in range(n):
        print("Hello, World!")


print_hello_world(5)
print("\n")


def print_hello_world(n):
    for i in range(1, n + 1):
        print("Hello, World!")


print_hello_world(5)
print("\n")


def print_hello_world(string, n=5):
    for i in range(1, n + 1):
        print(f"{string}")


print_hello_world("Hello, World!")
print("\n")


def print_hello_world(string, n=5):
    for i in range(1, n + 1):
        print(f"{string}")


print_hello_world("Hello, World!", 10)
