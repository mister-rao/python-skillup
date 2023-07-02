import typer
from peewee import *
from shop.models import create_tables, User, Inventory
from shop.authentication import UserSession, Authentication

from shop.exceptions import ShopYooExit

app = typer.Typer()

user_session = UserSession()
auth = Authentication(user_session)


@app.command()
def add_item(name: str, desc: str, price: int):
    item = Inventory.create(name=name, description=desc, price=price)
    typer.echo(f"Item added: {item.name} ({item.description})")


@app.command()
def list():
    items = Inventory.select()
    for item in items:
        typer.echo(
            f"iName: {item.name}, iDescription: {item.description}, iPrice : {item.price} "
        )


@app.command()
def signup(username: str, password: str):
    auth.signup(username=username, password=password)


@app.command()
def login(username: str, password: str):
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
        app()
