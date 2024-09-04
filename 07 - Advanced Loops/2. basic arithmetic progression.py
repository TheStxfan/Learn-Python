
def sum_up_to(numbers, step=1, start=1):
    result = 0
    for i in range(start, numbers+1, step):
        if i + step > numbers:
            print(i, end=" = ")
        else:
            print(i, end=" + ")
        result += i
    return result


print(sum_up_to(6))                             # 1 + 2 + 3 + 4 + 5 + 6 = 21
print(sum_up_to(15, 2))            # 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64
print(sum_up_to(14, start=5))           # 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 = 95
print(sum_up_to(100, 10, 5))  # 5 + 15 + 25 + 35 + 45 + 55 + 65 + 75 + 85 + 95 = 500
