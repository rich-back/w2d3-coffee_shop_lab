class CoffeeShop:
    

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def made_drinks(self):
        return len(self.drinks)

    def make_drink(self, drink_name):
        self.drinks.append(drink_name)
    
    def clear_drink(self):
        self.drinks.clear()

