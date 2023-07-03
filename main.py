import typer
from peewee import *
from shop.models import create_tables
from shop.services.authentication import UserSession, Authentication
from shop.services.inventory import ShopInventory
from shop.exceptions import ShopYooExit

from shop.commands import users, inventory, cart

app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="users")
app.add_typer(inventory.app, name="inventory")
app.add_typer(cart.app, name="cart")


if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()
