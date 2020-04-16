import pandas as pd

groceries = pd.Series(data=[30,6,'Yes','No'], index=['eggs','apples','milk','bread'])
print(groceries)

print('shape: ', groceries.shape)
print('dimension: ', groceries.ndim)
print('total: ', groceries.size, 'elements')

print('data: ', groceries.values)
print('index: ', groceries.index)

x = 'bananas' in groceries
print(x)