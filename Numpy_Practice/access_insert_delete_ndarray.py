import numpy as np

'''
# rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])


print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0])
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])
'''

'''
# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print X
print()
print('X = \n', X)
print()

# Let's access some elements in X
print('This is (0,0) Element in X:', X[0,0])
print('This is (0,1) Element in X:', X[0,1])
print('This is (2,2) Element in X:', X[2,2])
'''

'''
x = np.array([1,2,3,4,5])


y = np.array([[1,2,3], [4,5,6], [7,8,9]])

print('original x = ', x)

x = np.delete(x,[0,2,4])

print('modified x = ', x)

print('original y = \n', y)

# delete the first row of y
w = np.delete(y, [0,2], axis=0)  # axis = 0 means row
print('modified w = \n', w)

# delete the first and last column of y
v = np.delete(y,[0,2], axis=1)
print('modified v= \n', v)
'''

'''
x = np.array([1, 2, 3, 4, 5])

y = np.array([[1,2,3],[4,5,6]])

print()
print('Original x = ', x)

# rank 1 ndarray
x = np.append(x, 6)
print(x)
x = np.append(x, [7,8,20])
print(x)

# rank 2 ndarray and add a new row
v = np.append(y, [[7,8,9]], axis=0)
print('v = \n', v)

# add column
q = np.append(y, [[9], [10]], axis=1)
print('q = \n', q)
'''

'''
# np.insert(ndarray, index, elements, axis)

x = np.array([1, 2, 3, 5, 6, 7])

y = np.array([[1,2,3],[7,8,9]])

print('Original x = ', x)

x = np.insert(x, 2, [11,12])
print('modified x =\n', x)

print('Original y = \n', y)
w = np.insert(y,1,[4,5,6], axis=0)
print('modified w = \n', w)

v = np.insert(y,1,55, axis=1)
print('modified v = \n', v)

v = np.insert(y,1,[77, 88], axis=1)
print('modified v = \n', v)
'''

# stacking np.vstack(), np.hstack()


x = np.array([1,2])

y = np.array([[3,4],[5,6]])

print('x = ', x)
print('y = \n', y)

z = np.vstack((x,y))
print('z = ', z)

w = np.hstack((y,x.reshape(2,1)))
print('w = \n', w)



