def ask_for_operation():
    print(
        "\nChoose an operation:\n",
        "1 - Addition\n",
        "2 - Subtraction\n",
        "3 - Multiplication\n",
        "4 - Division\n",
        "5 - Exit")

    choice = input("Operation choice: ")
    return choice


def calculate_result(first_number, second_number, operation_number):
    result = int()
    if operation_number == 1:
        result = first_number + second_number
    elif operation_number == 2:
        result = first_number - second_number
    elif operation_number == 3:
        result = first_number * second_number
    elif operation_number == 4:
        result = first_number / second_number
    elif operation_number == 5:
        exit()
    return result


def print_result(n):
    print(f"\nResult is {n}. \n")


while True:
    number1 = int(input("Enter Number 1: "))
    number2 = int(input("Enter Number 2: "))

    operation = 0
    first_time = True

    while operation not in {1, 2, 3, 4, 5}:
        if not first_time:
            print("\nInvalid operation choice. Please try again.")
        operation = int(ask_for_operation())
        first_time = False

    final_result = calculate_result(number1, number2, operation)

    print_result(final_result)
