from items import Menu, spacer, Bowl, Scoop, Flavour
# [OK] list of available flavours
# [OK] cost of each flavour - from menu
# quantity - what flavour, how many each ? 
#   - select flavor, add quantity (scoop)--> add to bowl
#   - bowl fills
#   - flavour grams reduce
# availablility of flavour
# offers
# ice cream combos

# nouns / classes - Flavour, IceCreamShop, 
#                   Offers, Menu (Combos),
#                   Bowl(bowl_size), Scoop

class IceCreamShop:
    menu = Menu()
    bowl = Bowl(2, 'Round')
    scoop = Scoop(10, 'small')
    
    def welcome(self):
        print('Hello, Welcome to our ice cream shop')
        choice = input('Do you want to see the menu? y/n >> ')
        if choice == 'y':
            self.menu.display()
        elif choice == 'n':
            print('maybe next time')
        else:
            print('We dont speak that language')
              
       
    def list_flavours(self):
        spacer()
        flavours = self.menu.get_flavours()
        print(f'{flavours=}')
        spacer()
        
    def order_icecream(self, ic_name, no_of_scoops):
        # select flavor, quantity
        # take scoop from menu
        for ic in self.menu.ice_creams:
            if ic.name == ic_name:
                if ic.quantity < self.scoop.size:
                    print('Flavour got over')
                    break
                self.scoop = self.take_scoop(ic, self.scoop)
                self.bowl.add_scoop(self.scoop.pour())
                

        print(f'Your Ice cream Bowl :: {self.bowl.contents}')
                    
                

        # add to bowl
        # reduce from menu

    def take_scoop(self, icecream: Flavour, scoop: Scoop):
        icecream.quantity = icecream.quantity - scoop.size
        scoop.scoop_flavor = icecream.name
        for i, ic in enumerate(self.menu.ice_creams):
            if ic.name == icecream.name:
                self.menu.ice_creams[i] = icecream
        return scoop
        


             




