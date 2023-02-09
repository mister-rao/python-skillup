# fruits - {price, quantity, name, discount}
# order - {amount, [fruits], time it takes, discount}
# 
# flow:
    # [OK] open the app
    # [OK] check what fruits are available
    # [OK] check discounts
    # [OK] add to cart - {name, quantity}
            # - enter fruit name, and quantity
            # - order more than one till done
    # [] check my cart
    # [] place the order, add location
    # [] confirm 
    
# data types:
# fruit - dict | key - fruit_name | values - {quantity, price, discount}
# order cart - | key - fruit_name | values - {quantity}


stock = {
    'apple' : {'quantity': 100, 'price': 100, 'discount': 2},   
    'pineapple' : {'quantity': 100, 'price': 100, 'discount': 15},   
    'watermelon' : {'quantity': 100, 'price': 100, 'discount': 20},   
    'banana' : {'quantity': 100, 'price': 100, 'discount': 30},   
    'strawberry' : {'quantity': 100, 'price': 100, 'discount': 5},   
}

cart = {} # {'fruit': 'quantity'}


def display_fruits(stock):
    print('fruit\t\tqunatity\tprice\tdiscount')
    for fruit, detail in stock.items():
        print(f"{fruit}\t\t{detail['quantity']}\t{detail['price']}\t{detail['discount']}")

def check_discounts(stock, minimum = 10):
    print('Getting you the best discounts!')
    for fruit, detail in stock.items():
        if detail['discount'] >= minimum:
            print(f"{fruit=} - {detail['discount']}%")

def order_fruit():
    is_ordering = True
    orders = {}
    print('Type DONE when you are done ordering!')
    while(is_ordering):
        order_input = input('Enter fruit name & quantity > ')
        try:
            fruit_name, quantity = order_input.split(' ')
        except:
            if order_input == 'DONE':
                is_ordering = False
                break
            else:
                print('Invalid fruit name, enter DONE to exit')
        
        print(fruit_name, quantity)
        orders[fruit_name] = quantity
    return orders




if __name__ == '__main__':
    choices = {
        '1' : 'Disply availbe fruits stock',
        '2': 'Check the best discounts',
        '3': 'Ready to order ?',
        '4': 'Check cart',
    }
    for i, _choice in choices.items():
        print(f'{i} - {_choice}')
    choice = input('Enter choice: ')
    
    if choice == '1':
        print(f'Entered choice is One, displying all fruits')
        display_fruits(stock)
    if choice == '2':
        check_discounts(stock, 5)
    if choice == '3':
        my_orders = order_fruit()
        print(f'my orders : {my_orders}')
    if choice == '4':
        print('Check my cart')
    
    else:
        print('Invalid choice')
    
    
    
    










