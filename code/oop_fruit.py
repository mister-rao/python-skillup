# Object Oriented Programming
# classes ---> objects (instances)
# classes - Stock, Fruit, Order, Cart, Shop, 

class Fruit:
    name: str
    is_ripe: bool
    
    def __init__(self, name, is_ripe=False) -> None:
        self.name = name
        self.is_ripe = is_ripe
        
    def wait_to_ripe(self):
        self.is_ripe = True

class Stock:
    """
    Functionalities:
        1. quantity of each fruit
        2. size
        3. add fruits (restock)
        4. remove fruits (sell)
        5. check inventory  
    """
    max_size = 200
    items = []
    
    def __init__(self, size=200) -> None:
        self.max_size = size
        
    def add_fruits(self, name, quantity):
        # add item to the stock by name
        if (len(self.items) >= self.max_size) or (quantity > self.max_size):
            print('Stock is full, or no space available')
            return

        self.items += [Fruit(name)] * quantity
    
    
    def check_inventory(self):
        # display fruit name and quanity
        raise NotImplementedError('Not implemented')
        
    def remove_fruits(self, fruit, quantiy):
        # remove fruits from items
        raise NotImplementedError('Not implemented')
    
    
    def display_items(self):
        if len(self.items) == 0:
            print('Stock is empty')
        else:
            print([fruit.name for fruit in self.items])
        
        
stock = Stock(size=20)
stock.add_fruits('Apple', 25)
stock.display_items()













