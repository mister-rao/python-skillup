from typing_extensions import Annotated
import typer
from shop.services.cart import UserCart
from shop.commands import users

app = typer.Typer()

auth = users.auth
cart = UserCart()


@app.command()
def add_to_cart(
    name: Annotated[str, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    cart.add_item(auth.user, name, quantity)
    # Prompt user for additional input
    add_more = typer.prompt("Add more items [y/n] ?", default="n")
    if add_more == "y":
        typer.run(add_to_cart)


@app.command()
def display():
    cart.display(auth.user)
