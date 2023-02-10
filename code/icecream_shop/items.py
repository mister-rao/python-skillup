
def spacer():
    print('-' * 20)


class Scoop:
    size: int  # quantity in grams
    scoop_type: str
    scoop_flavor: str 
    
    def __init__(self, size, scoop_type) -> None:
        self.size = size
        self.scoop_type = scoop_type
        
    def pour(self):
        flavour = self.scoop_flavor
        self.scoop_flavor = ''
        return flavour
        
        

class Bowl:
    size: int # number of scoops it can hold
    shape: str # shape of the bowl
    contents = [] # contents of the bowl
    
    def __init__(self, size, shape) -> None:
        self.size = size
        self.shape = shape
    
    def add_scoop(self, scoop):
        # add scoop to the content
        self.contents.append(scoop)

        

class Flavour:
    name: str 
    quantity: int  # quantity in grams
    price: int   # price per scoop

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    
    def __repr__(self) -> str:
        return self.name
    
    def details(self):
        print(f'{self.name} remaining: {self.quantity} grams')
        
    def menu_details(self):
        print(f'{self.name} Rs. {self.price} per scoop')

class Menu:
    # price
    # list of ice creams
    ice_creams = []
    combos = []
    
    def __init__(self) -> None:
        flavour_1 = Flavour('vanilla', 1000, 60)
        flavour_2 = Flavour('chocolate', 1000, 60)
        flavour_3 = Flavour('strawberry', 1000, 60)
        flavour_4 = Flavour('butterscotch', 1000, 60)
        flavour_5 = Flavour('tender-coconut', 1000, 60)
        self.ice_creams = [flavour_1,flavour_2, flavour_3, flavour_4, flavour_5]
        self.combos = [
            [flavour_1, flavour_2, flavour_5],
            [flavour_1, flavour_3],
            [flavour_2, flavour_3, flavour_5],
            [flavour_1, flavour_2, flavour_1]
        ]
    
    
    def display_inventory(self):
        spacer()
        print('These ice creams are available: ')
        for ice_cream in self.ice_creams:
            ice_cream.details()
        spacer()
        
    def display(self):
        spacer()
        print('These ice creams are available: ')
        for ice_cream in self.ice_creams:
            ice_cream.menu_details()
        spacer()


    def display_combos(self):
        for combo in self.combos:
            print(combo)
            
    def get_flavours(self):
        return self.ice_creams
