from decimal import Decimal
from collections import defaultdict


class NforY:
    def __init__(self, item, quantity, price):
        if not (isinstance(price, Decimal) or isinstance(price, int)):
            raise ValueError("Prices must be instances of Decimal or int")

        if quantity < 1:
            raise ValueError("Invalid quantity")

        self.item = item
        self.quantity = quantity
        self.price = price

    def apply(self, num_in_cart):
        quotient, remainder = divmod(num_in_cart, self.quantity)
        return Decimal(quotient * self.price), remainder


class UnitPrice(NforY):
    def __init__(self, item, price):
        super().__init__(item, 1, price)

class PricingRules:
    def __init__(self, rules):
        self.rules = defaultdict(list)
        for rule in rules:
            self.rules[rule.item].append(rule)