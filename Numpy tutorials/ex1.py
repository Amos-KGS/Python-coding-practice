import numpy as np

# defining our array sequentially
a = np.arange(15).reshape(3, 5)
print("The array appears as:\n ", a)

# Get the array shape(rows by columns)
print("The array shape is: ", a.shape)

# to get the array dimensions.
print("The array dimensions is: ", a.ndim)

# to get array size
print("Size of the array is: ", a.size)

# to get the library type used
print("Array library type used: ",type(a))
