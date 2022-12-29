from decimal import Decimal

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
        