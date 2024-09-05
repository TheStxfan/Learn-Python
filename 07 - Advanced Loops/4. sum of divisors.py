# 1
def sum_of_divisors(number):
    divisors = []
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)

    result = 0
    total_divisors = len(divisors)
    for divisor in divisors:
        if divisor == divisors[-1]:
            print(divisor, end=" = ")
        else:
            print(divisor, end=" + ")
        result += divisor

    return result


print(sum_of_divisors(15))  # 1 + 3 + 5 + 15 = 24


# 2
def sum_of_divisors(number):
    result = 0
    for divisor in range(1, number+1):
        if number % divisor == 0:
            result += divisor
            if divisor == number:
                print(divisor, end=" = ")
            else:
                print(divisor, end=" + ")

    return result


print(sum_of_divisors(20))  # 1 + 2 + 4 + 5 + 10 + 20 = 42
