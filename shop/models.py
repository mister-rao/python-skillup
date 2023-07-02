"""
This file contains database models for the shopyoo app.
Models represent tables in the database and the relationship b/w them.
"""

from peewee import *


# database connection
db = SqliteDatabase("shopyoo.db")


class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Inventory(Model):
    name = CharField()
    description = CharField()
    price = IntegerField()

    class Meta:
        database = db


class Cart(Model):
    user = ForeignKeyField(User)
    items = ManyToManyField(Inventory)


class Order(Model):
    user = ForeignKeyField(User)
    items = ManyToManyField(Inventory)
    amount = FloatField()
    payment_mode = CharField()


def create_tables():
    # create tables
    with db:
        db.create_tables([User, Inventory])
