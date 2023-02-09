# available fruits
# fruits 
# add fruits
# remove fruits

available_fruits = ['apple', 'banana', 'papaya', 'watermelon',]
my_basket = []

def add_fruit(basket, fruit, quantity):
    if fruit in available_fruits:
        print(f'adding {quantity} {fruit}s to basket')
        basket += [fruit] * quantity
    else:
        print('fruit not available')
    return basket

def remove_fruit(basket, fruit, quantity):
    if fruit in basket:
        print(f'Removing {quantity} {fruit}s')
        for f in basket:
            if f == fruit and quantity > 0:
                basket.remove(fruit)
                quantity = quantity - 1
    else:
        print('Fruit not in basket')
    return basket


my_basket = add_fruit(my_basket, 'apple', 3)
my_basket = add_fruit(my_basket, 'banana', 4)
print(my_basket)

my_basket = remove_fruit(my_basket, 'apple', 2)
print(my_basket)


