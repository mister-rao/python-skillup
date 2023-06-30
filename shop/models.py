"""
This file contains database models for the shopyoo app.
Models represent tables in the database and the relationship b/w them.
"""

from peewee import *
from shop import db

class User(Model):
    username = CharField(unique=True)

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
    
