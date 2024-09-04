def sum_of_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    result = 0
    for divisor in divisors:
        result += divisor

    return result


print(sum_of_divisors(15))
