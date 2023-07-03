from typing_extensions import Annotated
import typer
from shop.services.inventory import ShopInventory

inventory = ShopInventory()

app = typer.Typer()


@app.command()
def restock(
    name: Annotated[str, typer.Option(prompt=True)],
    price: Annotated[int, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    inventory.restock(name, price, quantity)
    # Prompt user for additional input
    more = typer.prompt("Add more stock [y/n] ?", default="n")
    if more == "y":
        typer.run(restock)


@app.command()
def display():
    inventory.display()
