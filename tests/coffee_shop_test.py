import unittest
from src.drinks import Drink
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00)
        self.drinks = Drink("Mocha", 2.50)

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(20.00)
        self.assertEqual(120.00, self.coffee_shop.till)

    def test_drinks_stock_level(self):
        self.assertEqual(0, self.coffee_shop.made_drinks())

    def test_can_make_drink(self):
        self.coffee_shop.make_drink(self)
        self.assertEqual(1, self.coffee_shop.made_drinks())

    def test_can_clear_drink(self):
        self.coffee_shop.make_drink(self.drinks)
        self.coffee_shop.clear_drink()
        self.assertEqual(0, self.coffee_shop.made_drinks())
        


        