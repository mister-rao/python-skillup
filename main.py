import typer
from peewee import *
from shop.models import create_tables
from shop.services.authentication import UserSession, AuthenticationService
from shop.services.inventory import InventoryService
from shop.exceptions import ShopYooExit

from shop.commands import users, inventory, cart, order

app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="users")
app.add_typer(inventory.app, name="inventory")
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")


if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()
