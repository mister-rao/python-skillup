from shop.models import Cart, Inventory
from shop.exceptions import ShopYooExit
from rich.console import Console
from rich.table import Table

console = Console()


class CartService:
    def add_item(self, user, name: str, quantity: int):
        cart_item: Cart = self.get_cart_item(user=user, name=name)
        Inventory.pick_item(name, quantity)
        cart_item.add(quantity=quantity)

    def remove_item(self, user, name: str, quantity: int):
        cart_item: Cart = self.get_cart_item(user=user, name=name)
        cart_item.remove(quantity=quantity)
        Inventory.drop_item(name, quantity)

    @staticmethod
    def get_cart_item(user, name: str) -> Cart:
        item = Inventory.get(name=name)
        try:
            cart_item = Cart.get(item=item, user=user)
        except Cart.DoesNotExist:
            cart_item = Cart.create(item=item, user=user, quantity=0)
        return cart_item

    def display(self, user):
        cart = Cart.filter(user=user)
        count = cart.count()

        if count == 0:
            print("Your cart looks empty, add some items!")
            return

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
        total_price = self.total_price(cart)
        print(f"Total items: {count} | price: Rs. {total_price}")

    def total_price(self, cart):
        price = 0
        for i in cart:
            price = price + (i.quantity * i.item.price)
        return price

    def clear(self, user):
        cart_items = Cart.filter(user=user)
        query = Cart.delete().where(Cart.id.in_(cart_items))
        query.execute()
