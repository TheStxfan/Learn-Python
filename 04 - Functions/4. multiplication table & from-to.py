
def print_multiplication_table(table):
    for i in range(1, 11):
        print(f"{table} * {i} = {table * i}")


print_multiplication_table(7)
print("\n")


def print_multiplication_table(table, start=1, end=10):
    for i in range(start, end+1):
        print(f"{table} * {i} = {table * i}")


print_multiplication_table(7, 1, 6)
print("\n")
print_multiplication_table(7)
