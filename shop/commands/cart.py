from typing_extensions import Annotated
import typer
from shop.services.cart import CartService
from shop.commands import users

app = typer.Typer()

auth = users.auth
cart = CartService()


@app.command()
def add(
    name: Annotated[str, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    cart.add_item(auth.user, name, quantity)
    display()


@app.command()
def remove(
    name: Annotated[str, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    cart.remove_item(auth.user, name, quantity)
    display()


@app.command()
def clear():
    cart.clear(auth.user)
    display()


@app.command()
def display():
    cart.display(auth.user)
