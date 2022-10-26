import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drinks import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("Jeff Bridges", 150)

    def test_customer_has_name(self):
        self.assertEqual("Jeff Bridges", self.customer1.name)

    def test_customer_has_money(self):
        self.assertEqual(150, self.customer1.wallet)

    def test_reduce_wallet(self):
        self.customer1.reduce_wallet(2.50)
        self.assertEqual(147.50, self.customer1.wallet)

    def test_customer_has_no_drink(self):
        self.assertEqual(0, len(self.customer1.drink_count))

    def test_customer_has_drink(self):
        self.customer1.add_drink(self)
        self.assertEqual(1, len(self.customer1.drink_count))

    def test_can_customer_buy_drink(self):
        drink1 = Drink("Mocha", 2.50)
        coffee_shop_name = CoffeeShop("The Prancing Pony", 100.00)
        coffee_shop_name.make_drink(drink1)
        self.customer1.add_drink(drink1)
        self.customer1.reduce_wallet(drink1.price)
        coffee_shop_name.increase_till(drink1.price)
        self.assertEqual(1, self.customer1.check_drink_count())
        coffee_shop_name.clear_drink()
        self.assertEqual(0, len(coffee_shop_name.drinks))

