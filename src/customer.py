class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drink_count = []


    def check_over_16(self, age):
        self.age >= 16

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def add_drink(self, drink_name):
        self.drink_count.append(drink_name)
        
    def check_drink_count(self):
        return len(self.drink_count)


