from shop.services.cart import CartService
from shop.models import Cart, Order
from rich.console import Console
from rich.table import Table

console = Console()


class OrderService:
    def __init__(self, cart_service: CartService) -> None:
        self.cart_service = cart_service

    def place(self, user):
        self.cart_service.display(user)
        cart = Cart.filter(user=user)

        orders = [
            Order(
                item=ci.item,
                quantity=ci.quantity,
                amount=ci.quantity * ci.item.price,
                user=ci.user,
                payment_mode="cash",
            )
            for ci in cart
        ]
        Order.bulk_create(orders)
        self.cart_service.clear(user)

    def checkout(self):
        pass

    def display(self, user):
        cart = Order.filter(user=user)
        table = Table("sl.No.", "Item", "Quantity", "Amount")
        for i, o in enumerate(cart):
            table.add_row(
                f"{i + 1}",
                o.item.name,
                str(o.quantity),
                f"Rs. {o.amount}",
            )
        console.print(table)
