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

        for item, rules in self.rules.items():
            self.rules[item] = sorted(rules,
                                      key=lambda r: (r.quantity, r.price),
                                      reverse=True)

            prices = [r.price for r in self.rules[item]]
            if any(x < y for x, y in zip(prices, prices[1:])):
                raise ValueError("Prices are decreasing")

            smallest_quantity = self.rules[item][-1].quantity
            if smallest_quantity > 1:
                raise ValueError("Must provide unit price")

    def total_for_item(self, item, quantity):
        result = Decimal(0)
        for rule in self.rules[item]:
            subtotal, quantity = rule.apply(quantity)
            result += subtotal
        assert quantity == 0
        return result

    def total(self, item_quantities):
        result = Decimal(0)
        for item, quantity in item_quantities.items():
            result += self.total_for_item(item, quantity)
        return result
