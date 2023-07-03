"""
This file contains database models for the shopyoo app.
Models represent tables in the database and the relationship b/w them.
"""

from email.policy import default
from peewee import *
from shop.exceptions import ShopYooExit


# database connection
db = SqliteDatabase("shopyoo.db")


class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Inventory(Model):
    name = CharField(unique=True)
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.price} {self.quantity}"

    @staticmethod
    def availability(name: str, quantity: int):
        item = Inventory.get(name=name)
        if item.quantity < quantity:
            raise ShopYooExit(f"Only {item.quantity} {name} available.")
        return item

    @staticmethod
    def pick_item(name: str, quantity: int):
        item = Inventory.availability(name, quantity)
        item.quantity = item.quantity - quantity
        item.save()

    @staticmethod
    def drop_item(name: str, quantity: int):
        item = Inventory.get(name=name)
        item.quantity = item.quantity + quantity
        item.save()

    def update_stock(self, price: int, quantity: int):
        self.update_price(price)
        self.update_quantity(quantity)
        self.save()
        print(f"{self.name} restocked!")

    def update_price(self, price: int):
        if self.price != price:
            self.price = price
            print(f"{self.name} price updated!")

    def update_quantity(self, quantity: int):
        self.quantity += quantity
        print(f"{self.name} quantity updated!")


class Cart(Model):
    user = ForeignKeyField(User)
    item = ForeignKeyField(Inventory)
    quantity = IntegerField()

    class Meta:
        database = db

    def add(self, quantity: int):
        self.quantity = self.quantity + quantity
        self.save()

    def remove(self, quantity: int):
        self.quantity = self.quantity - quantity
        self.save()
        if self.quantity == 0:
            self.delete_instance()


class Order(Model):
    user = ForeignKeyField(User)
    item = ForeignKeyField(Inventory)
    quantity = IntegerField()
    amount = FloatField()
    payment_mode = CharField()
    status = CharField(default="pending")

    class Meta:
        database = db


def create_tables():
    # create tables
    with db:
        db.create_tables([User, Inventory, Cart, Order])
