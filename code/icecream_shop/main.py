from shop import IceCreamShop

# list of available flavours
# cost of each flavour
# quantity - what flavour, how many each ? 
# availablility of flavour
# offers
# ice cream combos

# nouns / classes - Flavour, IceCreamShop, 
#                   Offers, Menu (Combos),
#                   Bowl(bowl_size), Scoop


choices = {
    '0': 'Exit',
    '1': 'Display menu',
    '2': 'List flavours',
    '3': 'Order chocoloate icecream',
    '9': 'Show inventory'
}



if __name__ == '__main__':
    is_entered_shop = True
    shop = IceCreamShop()
    
    while(is_entered_shop):
        for choice, desc in choices.items():
            print(choice, desc)
        
        input_ch = input('Enter your choice >> ')
        
        if input_ch == '0':
            print('Thank you, visit again')
            is_entered_shop = False
            break
        
        if input_ch == '1':    
            shop.welcome()
            
        if input_ch == '2':
            shop.list_flavours()
            
        if input_ch == '3':
            shop.order_icecream('chocolate', 2)
        
        if input_ch == '9':
            shop.menu.display_inventory()