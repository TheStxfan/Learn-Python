
# todo : create the geometric progression calculator

def sum_up_to(numbers, step=1, start=1):
    result = 0
    for i in range(start, numbers+1, step):
        if i + step > numbers:
            print(i, end=" = ")
        else:
            print(i, end=" x ")
        result *= i
    return result


print(sum_up_to(10))		 # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
print(sum_up_to(20, 2))		 # 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
print(sum_up_to(60, 10, 5))	 # 5 + 15 + 25 + 35 + 45 + 55 = 180
