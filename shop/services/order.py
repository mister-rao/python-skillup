from shop.commands.cart import display
from shop.services.cart import CartService
from shop.models import Cart, Order
from rich.console import Console
from rich.table import Table
from shop.exceptions import ShopYooExit

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

    def checkout(self, user, amount):
        orders = Order.filter(user=user, status="pending")
        if orders.count() == 0:
            raise ShopYooExit("Place your order before checking out!")

        total_price = self.cart_service.total_price(orders)
        change = 0
        if amount > total_price:
            change = amount - total_price
        if amount < total_price:
            raise ShopYooExit("Insufficient balance")

        for o in orders:
            o.status = "paid"
            o.save()

        print("Items bought: ")
        self.display(user, "paid")
        print(f"Here's your change: {change}")

    def history(self, user):
        orders = Order.filter(user=user, status="paid")
        if orders.count() == 0:
            raise ShopYooExit("You have not bought anythin yet.")
        print("Here's your order history:")
        self.display(user, "paid")

    def display(self, user, o_status="pending"):
        orders = Order.filter(user=user, status=o_status)
        count = orders.count()
        table = Table("sl.No.", "Item", "Quantity", "Amount")
        for i, o in enumerate(orders):
            table.add_row(
                f"{i + 1}",
                o.item.name,
                str(o.quantity),
                f"Rs. {o.amount}",
            )
        console.print(table)
        total_price = self.cart_service.total_price(orders)
        print(f"Total items: {count} | price: Rs. {total_price}")
