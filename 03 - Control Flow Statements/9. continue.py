keep_going_after_check_1 = False   # True or False | 1 or 0
keep_going_after_check_2 = 1   # True or False | 1 or 0

# 1 - for loop
for i in range(0, 99, 1):
    i += 1
    print(i)

    if i == 50:
        print("End of for loop")
        if keep_going_after_check_1:  # if variable, checks if that variable is true
            continue
        else:                         # if it is not, it lets the loop continue
            break

print()

# 2 - infinite while loop
i = 0
while True:
    i += 1
    print(i)
    if i == 50:
        print("End of while loop")
        if keep_going_after_check_2:
            continue
        else:
            break
