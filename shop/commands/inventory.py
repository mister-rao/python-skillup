from typing_extensions import Annotated
import typer
from shop.services.inventory import InventoryService

inventory = InventoryService()

app = typer.Typer()


@app.command()
def restock(
    name: Annotated[str, typer.Option(prompt=True)],
    price: Annotated[int, typer.Option(prompt=True)],
    quantity: Annotated[int, typer.Option(prompt=True)],
):
    inventory.restock(name, price, quantity)


@app.command()
def display():
    inventory.display()
