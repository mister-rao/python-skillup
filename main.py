import typer
from peewee import *
from shop import db
from shop.models import Inventory

# create tables
with db:
    db.create_tables([Inventory])

app = typer.Typer()


@app.command()
def add_item(name: str, desc: str, price: int):
    item = Inventory.create(name=name, description=desc, price=price)
    typer.echo(f"Item added: {item.name} ({item.description})")



@app.command()
def list():
    items = Inventory.select()
    for item in items:
        typer.echo(f"iName: {item.name}, iDescription: {item.description}, iPrice : {item.price} ") 



@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()