from OOP.shirt import Shirt

new_shirt = Shirt('blue', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print('Price: {}'.format(new_shirt.price))

print('Discount: {}'.format(new_shirt.discount(.2)))

tshirt_collection =[]
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

for i in range(len(tshirt_collection)):
    print('Tshirt color: ' + tshirt_collection[i].color)


