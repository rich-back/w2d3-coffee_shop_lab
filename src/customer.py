class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drink_count = []

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def add_drink(self, drink_name):
        self.drink_count.append(drink_name)
        

    def check_drink_count(self):
        return len(self.drink_count)


