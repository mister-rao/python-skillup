from shop.models import Cart, Inventory
from shop.exceptions import ShopYooExit


class UserCart:
    def __init__(self, user) -> None:
        self.user = user

    def add_item(self, name: str, quantity: int):
        item = Inventory.get(name=name)
        if item.quantity < quantity:
            raise ShopYooExit(f"Only {item.quanity} {name} available.")
        Cart.create(item=item, quantity=quantity, user=self.user)

    def total_price(self):
        pass

    def display(self):
        pass
