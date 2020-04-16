import pandas as pd
import numpy as np

fruits = pd.Series(data=[10,6,3], index=['apples', 'oranges', 'bananas'])

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()

# use numpy
print('EXP(X) = \n', np.exp(fruits))
print()
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2

# arithmetic operations on selected items

print('Amount of Bananas + 2 = ', fruits['bananas'] + 2)
print()

print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

print('Amount of oranges + 4 = ', fruits.loc['oranges'] + 4)

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)

# mixed data type
groceries = pd.Series(data=[30,6,'Yes','No'], index=['eggs','apples','milk','bread'])
print(groceries * 2)

# important accessing elements
print(fruits.loc['oranges'])
print(fruits.loc[['oranges']])
print(fruits.iloc[0])
print(fruits.iloc[[0]])
