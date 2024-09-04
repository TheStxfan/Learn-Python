
def simple_interest(principal, interest, duration):
    current_year = principal
    for i in range(1, duration+1):
        current_year += (principal // 100) * interest
        print(current_year)

    print(f"\nLast year = {current_year}")


simple_interest(10000, 5, 5)
