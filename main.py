import typer
from peewee import *
from shop.models import create_tables, User, Inventory
from shop.authentication import UserSession, Authentication
from shop.inventory import ShopInventory
from shop.cart import UserCart
from shop.exceptions import ShopYooExit
from typing_extensions import Annotated

app = typer.Typer()

user_session = UserSession()
auth = Authentication(user_session)
inventory = ShopInventory()


@app.command()
def restock(
    name: Annotated[str, typer.Option(prompt=True)],
    price: Annotated[int, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    inventory.restock(name, price, quantity)
    # Prompt user for additional input
    more = typer.prompt("Add more stock [y/n] ?", default="n")
    typer.run(restock)


@app.command()
def add_to_cart(
    name: Annotated[str, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    cart = UserCart(auth.user)
    cart.add_item(name, quantity)
    # Prompt user for additional input
    add_more = typer.prompt("Add more items [y/n] ?", default="n")
    if add_more == "y":
        typer.run(add_to_cart)


@app.command()
def display():
    inventory.display()


@app.command()
def signup(
    username: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    auth.signup(username=username, password=password)


@app.command()
def login(
    username: str,
    password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
):
    auth.login(username=username, password=password)


@app.command()
def user():
    auth.check_session()


@app.command()
def logout():
    auth.logout()


if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()
