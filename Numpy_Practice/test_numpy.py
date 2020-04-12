import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)
print()

print(' dimension', x.shape)
print(' obj type ', type(x))
print(' elements ', x.dtype)

print('\n -------------------- \n')

y = np.array([[1,2,3],[5,6,7], [9,10,11.1]])
print()
print('Y = \n', y)
print()

print(' dimensions: ', y.shape)
print(' total size: ', y.size)
print(' obj type ', type(y))
print('type : ', y.dtype)

x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

print()
print(x)
print(x.dtype)


# save x into the current directory as
np.save('my_numpy_array', x)
