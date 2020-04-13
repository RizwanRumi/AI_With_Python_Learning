import numpy as np

'''
x = np.arange(20).reshape(4, 5)
print('x = \n', x)

# selected [row, col]
z = x[1:4, 2:5]
print('z = \n', z)
# another way
w = x[1:, 2:5]
print('w = \n', w)

# We select all the elements that are in the 1st through 3rd rows and
# in the 3rd to 4th columns
Y = x[:3, 2:5]
print('Y = \n', Y)

# select all the elements in the 3rd row
v = x[2,:]
print('v = ', v)
# select all the elements in the 3rd column
q = x[:,2]
print('q = ', q)

# select all the elements in the 3rd column but return a rank 2 ndarray
R = x[:, 2:3]
print('R = \n', R)
'''

# important : copy
# Z = X[1:4,2:5]
# the slice of the original array X is not copied in the variable Z.
# Rather, X and Z are now just two different names for the same ndarray.
# We say that slicing only creates a view of the original array.
# This means that if you make changes in Z you will be in effect changing
# the elements in X as well. Let's see

'''
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 4th columns
Z = X[1:4,2:5]

# We print Z
print()
print('Z = \n', Z)
print()

# We change the last element in Z to 555
Z[2,2] = 555

# We print X
print()
print('X = \n', X)
print()
'''

# We can clearly see in the above example that if we make changes to Z, X changes as well.
# However, if we want to create a new ndarray that contains a copy of the values
# in the slice we need to use the np.copy() function. The np.copy(ndarray) function
# creates a copy of the given ndarray. This function can also be used as a method,
# in the same way as we did before with the reshape function.
# Let's do the same example we did before but now with copies of the arrays.
# We'll use copy both as a function and as a method.

'''
X = np.arange(20).reshape(4, 5)

print('X = \n', X)

# create a copy of the slice using the np.copy() function
Z = np.copy(X[1:4, 2:5])

#  create a copy of the slice using the copy as a method
W = X[1:4, 2:5].copy()

# We change the last element in Z to 555
Z[2, 2] = 555

# We change the last element in W to 444
W[2, 2] = 444

print('X = \n', X)
print('Z = \n', Z)
print('W = \n', W)
'''
'''
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1,3])

# We print X
print()
print('X = \n', X)
print()
# We print indices
print('indices = ', indices)
print()

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)
'''

'''
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('X = \n', X)
print()

# We print the elements in the main diagonal of X
print('z =', np.diag(X))
print()

# We print the elements above the main diagonal of X
print('y =', np.diag(X, k=1))
print()

# We print the elements below the main diagonal of X
print('w = ', np.diag(X, k=-1))
print('w = ', np.diag(X, k=-2))
'''

'''
# Create 3 x 3 ndarray with repeated values
X = np.array([[1,2,3],[5,2,8],[1,2,3]])
print('X = \n', X)

# We print the unique elements of X
print('The unique elements in X are:',np.unique(X))
'''
