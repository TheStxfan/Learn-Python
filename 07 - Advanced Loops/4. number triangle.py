
def print_a_number_triangle(number):

    row = []
    for i in range(1, number+1):
        row.append(i)
        for number in range(1, len(row)+1):
            print(number, end=" ")
        print()


print_a_number_triangle(50)
input()