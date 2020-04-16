import pandas as pd
import os

# We create a dictionary of Pandas Series
items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series(data=[40, 110, 500, 45, 100], index=['book', 'glasses', 'bike', 'pants', 'shoes'])}

'''
# We print the type of items to see that it is a dictionary
print(type(items))

# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# display dataframe
print(shopping_carts)
print()

# print some information about shopping_carts
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)
'''
'''
# selected data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])
print(bob_shopping_cart)

# selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index=['pants', 'book'])
print(sel_shopping_cart)

# Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])
print(alice_sel_shopping_cart)
'''

# create a dictionary of lists (arrays) -- must be same length
data = {'Integers': [1, 2, 3],
        'Floats': [4.5, 8.2, 9.6]}

df = pd.DataFrame(data)
print(df)

# provide the row index
df = pd.DataFrame(data, index=['label 1', 'label 2', 'label 3'])
print(df)

# create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

store_items = pd.DataFrame(items2)
print(store_items)

# provide the row index
store_items = pd.DataFrame(items2, index=['store 1', 'store 2'])
print(store_items)
