from shop.models import Cart, Inventory
from shop.exceptions import ShopYooExit
from rich.console import Console
from rich.table import Table

console = Console()


class UserCart:
    def add_item(self, user, name: str, quantity: int):
        item = Inventory.get(name=name)
        if item.quantity < quantity:
            raise ShopYooExit(f"Only {item.quantity} {name} available.")
        cart_item, _ = Cart.get_or_create(item=item, user=user)
        cart_item.add(quantity=quantity)

    def total_price(self):
        pass

    def display(self, user):
        cart = Cart.filter(user=user)
        table = Table("sl.No.", "Item", "Quantity", "Price", "Amount")
        for i, ci in enumerate(cart):
            table.add_row(
                f"{i + 1}",
                ci.item.name,
                str(ci.quantity),
                f"Rs. {ci.item.price}",
                f"Rs. {ci.quantity * ci.item.price}",
            )
        console.print(table)
