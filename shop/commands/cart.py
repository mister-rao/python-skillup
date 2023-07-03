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
    auth.is_authenticated()
    cart.add_item(auth.user, name, quantity)
    display()


@app.command()
def remove(
    name: Annotated[str, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    auth.is_authenticated()
    cart.remove_item(auth.user, name, quantity)
    display()


@app.command()
def clear():
    auth.is_authenticated()
    print("This will remove all items from your cart.")
    if confirm := typer.confirm("Are you sure ?", default=False):
        cart.clear(auth.user)
        print("Cart emptied")


@app.command()
def display():
    auth.is_authenticated()
    cart.display(auth.user)
