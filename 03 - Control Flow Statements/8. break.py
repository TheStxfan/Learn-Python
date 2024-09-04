# 1 - for loop
for i in range(0, 99, 1):
    i += 1
    print(i)

    if i == 50:
        print("End of loop for loop\n")
        break


# 2 - infinite while loop
i = 0
while True:
    i += 1
    print(i)
    if i == 50:
        print("End of while loop")
        break
