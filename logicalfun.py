'''  Logical and statistical function 
Logical Functions in NumPy ----These functions are used for condition checking and return boolean (True/False) values.

logical_and() -- Performs element-wise logical AND operation between two arrays.   Parameters

x1 → First array/condition
x2 → Second array/condition

logical_or()-- Returns True if at least one condition is True.  
logical_not() -- Reverses boolean values (True → False, False → True).   Parameters x → Input array

all() -- Returns True if all elements are True.  Parameters  a → Input array  axis (optional)

any() -- Returns True if any element is True.  Parameters- a, axis (optional)

where() -- Returns elements based on a condition.  Parameters= condition  x → value if True   y → value if False

equal() -- Checks if elements of two arrays are equal.  Parameters=x1, x2

STATISTICAL FUNCTIONS -

np.mean() - Calculates the average of elements.  
Parameters
a → Input array
axis (optional)

np.median() - Returns the middle value after sorting.
Parameters
a
axis (optional)

np.std()= Calculates standard deviation (spread of data).
Parameters
a
axis (optional)

np.var()= Calculates variance of the dataset.
Parameters
a
axis (optional)

np.min() and np.max()
min() → smallest value
max() → largest value
a
axis (optional)

np.sum()= Returns sum of all elements.
Parameters
a
axis (optional)

np.percentile()= Finds the value below which a given % of data falls.
Parameters
a → array
q → percentile (0–100)

np.ptp()= Returns range (max - min)
Parameter
a

np.corrcoef()= Calculates correlation coefficient between arrays.
Parameters=
x, y

np.cov()=Calculates covariance matrix.
Parameters
x, y
'''

import numpy as np

a = np.array([1, 2, 3, 4])
result = np.logical_and(a>1,a<4)
print("and:",result)

result2 = np.logical_or(a>3,a<2)
print("or:",result2)

result3 = np.logical_not(a>2)
print("not:",result3)

a1 = np.array([True, True, False])
a2 = np.array([True, True, True])
print("all()",np.all(a1))
print("all():",np.all(a2))
print("any()",np.any(a1))

a3 = np.array([5, 10, 15, 20])
print("where()",np.where(a/2))

arr1 = np.array([10, 20, 30])
arr2 = np.array([10, 25, 30])

print("Equal or not:",np.equal(arr1,arr2))

print("Mean:",np.mean(a))

print("Median:",np.median(a))

print("Standard deviation:",np.std(a))

print("Variance:",np.var(a))

print("Minimum:",np.min(a))

print("Maximum:",np.max(a))

print("Percentile",np.percentile(a3,20))

print("Range",np.ptp(a3))

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
print("correlation cofficient",np.corrcoef(x,y))

print("Covarience matrix:",np.cov(x,y))


# 41. Find the unique values in a NumPy array.
u = np.array([1, 2, 2, 3, 4, 4, 5])
print("Unique values:",np.unique(u))

# 42. Count the occurrence of each unique value in a NumPy array.
values, counts = np.unique(a, return_counts=True)
print("counts:",counts)

#  Find the maximum and minimum values in a NumPy array.
print("Minimum:",np.min(u))
print("Maximum:",np.max(u))

# Get the index of the maximum value in an array.
# np.argmax() -- Returns the index of the maximum (largest) value in an array.

ab = np.array([10, 25, 15, 40, 30])
index = np.argmax(ab)
print("Index of maximum value",index)

# Get the index of the minimum value in an array
index1 = np.argmin(ab)
print("Index of minimum value",index1)

# Compute the cumulative sum of a NumPy array
# np.cumsum()-- Returns the cumulative (running) sum of elements in an array.

cum_sum = np.cumsum(ab)
print("Cumulativ sum:",cum_sum)

#  Compute the cumulative product of a NumPy array
cum_product = np.cumprod(ab)
print("Cumulativ product:",cum_product)

# Check if a NumPy array contains any NaN values
# np.isnan() → checks which elements are NaN (Not a Number)

# np.any() → returns True if any value is True

cd = np.array([1, 2, np.nan, 4])
result4 = np.any(np.isnan(cd))
print("Nan value:",result4)

#  Replace NaN values with 0 in a NumPy array.
# np.nan_to_num()-- Replaces NaN (Not a Number) values with a specified number (default = 0).
nan_value = np.array([1, 2, np.nan, 4, np.nan])
result5 = np.nan_to_num(nan_value)
print("Result:",result5)

#  Count the number of nonzero elements in an array.
# np.count_nonzero() -- Returns the number of elements that are not equal to zero in the array.

zero = np.array([0, 1, 2, 0, 3, 0, 4])
count = np.count_nonzero(zero)
print("Non zero element:",count)


