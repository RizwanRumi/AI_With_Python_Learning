# Mean Normalization

# In machine learning we use large amounts of data to train our models.
# Some machine learning algorithms may require that the data is *normalized* in order
# to work correctly. The idea of normalization, also known as *feature scaling*, is to
# ensure that all the data is on a similar scale, *i.e.* that all the data takes on a
# similar range of values. For example, we might have a dataset that has values
# between 0 and 5,000. By normalizing the data we can make the range of values be
# between 0 and 1.

# In this lab, you will be performing a different kind of feature scaling known as *mean normalization*.
# Mean normalization will scale the data, but instead of making the values be between 0 and 1,
# it will distribute the values evenly in some small interval around zero.
# For example, if we have a dataset that has values between 0 and 5,000, after mean normalization
# the range of values will be distributed in some small range around 0,
# for example between -3 to 3. Because the range of values are distributed evenly around zero,
# this guarantees that the average (mean) of all elements will be zero.
# Therefore, when you perform *mean normalization* your data will not only be scaled
# but it will also have an average of zero.

# To Do:
# You will start by importing NumPy and creating a rank 2 ndarray of random integers
# between 0 and 5,000 (inclusive) with 1000 rows and 20 columns. This array will simulate
# a dataset with a wide range of values.

# Solution: (only match the result purpose)
# https://q10viking.gitee.io/2018/12/24/181224-Mean-Normalization-and-Data-Separation/


# import NumPy into Python
import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0, 5001, size=(1000, 20))

# print the shape of X
print(X)

# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# If you have done the above calculations correctly, then ave_cols and std_cols, should both 
# be vectors with shape (20,) since  𝑋  has 20 columns. You can verify this by filling the code below:

# Print the shape of ave_cols
print(ave_cols.shape)

# Print the shape of std_cols
print(std_cols.shape)

# Mean normalize X
X_norm = (X - ave_cols) / std_cols

# Print the average of all the values of X_norm
print('average of all the values: ', X_norm.mean())

# Print the average of the minimum value in each column of X_norm
print('average of the minimum value in each column: ', X_norm.min(axis=0))

# Print the average of the maximum value in each column of X_norm
print('average of the maximum value in each column: ', X_norm.max(axis=0))

# Data Separation

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.random.permutation(1000)

# Make any necessary calculations.
# You can save your calculations into variables to use later.


# Create a Training Set
X_train = X_norm[row_indices[0:600]]

# Create a Cross Validation Set
X_crossVal = X_norm[row_indices[600:800]]

# Create a Test Set
X_test = X_norm[row_indices[800:1000]]

# Print the shape of X_train
print('X_train: ', X_train.shape)

# Print the shape of X_crossVal
print('X_crossVal: ', X_crossVal.shape)

# Print the shape of X_test
print('X_test: ', X_test.shape)


