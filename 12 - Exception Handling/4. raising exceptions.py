class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception('Currencies Do Not Match')
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


value1 = Currency('USD', 20)
value2 = Currency('USD', 30)
print("1.", value1 + value2)

value3 = Currency('USD', 20)
value4 = Currency('EUR', 30)
print("2.", value3 + value4)
