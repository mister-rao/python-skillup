from typing_extensions import Annotated
import typer
from shop.services.cart import CartService
from shop.services.order import OrderService
from shop.commands import users

app = typer.Typer()
cart = CartService()
order = OrderService(cart)
auth = users.auth


@app.command()
def place():
    order.place(auth.user)


@app.command()
def display():
    order.display(auth.user)
