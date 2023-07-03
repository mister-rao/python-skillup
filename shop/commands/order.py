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
    auth.is_authenticated()
    order.place(auth.user)


@app.command()
def display():
    auth.is_authenticated()
    order.display(auth.user)


@app.command()
def history():
    auth.is_authenticated()
    order.history(auth.user)


@app.command()
def checkout(amout: int):
    auth.is_authenticated()
    order.checkout(auth.user, amout)
