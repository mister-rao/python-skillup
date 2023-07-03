from shop.models import Inventory
import peewee as pwee
from rich.console import Console
from rich.table import Table

console = Console()


class InventoryService:
    def restock(self, name: str, price: str, quantity: int):
        try:
            stock = Inventory.create(name=name, price=price, quantity=quantity)
        except pwee.IntegrityError:
            stock: Inventory = Inventory.get(name=name)
            stock.update_stock(price, quantity)

    def display(self):
        stock = Inventory.select()

        table = Table("sl.No.", "Name", "Price", "Avail. Quantity", "Item-id")
        for i, item in enumerate(stock):
            table.add_row(
                f"{i + 1}",
                item.name,
                f"Rs. {item.price}",
                str(item.quantity),
                str(item.id),
            )

        console.print(table)
