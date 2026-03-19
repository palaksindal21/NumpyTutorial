'''
Searching and Sorting
Searching in Numpy--
Searching means finding positions, indices, or elements based on conditions.
1. np.where() – Returns indices where a condition is True.
Parameters
condition
x (optional) → value if True
y (optional) → value if False

2. np.argmax() and np.argmin()
argmax() → index of maximum value
argmin() → index of minimum value

Parameters
a → Input array
axis (optional)

3. np.nonzero()– Returns indices of non-zero elements.
Parameters
a → Input array

4. np.searchsorted() – Finds index where element should be inserted to maintain sorted order.

Parameters
a → Sorted array
v → Value to insert

5. np.extract() – Returns elements satisfying a condition.

Parameters
condition
a → Input array

Sorting in NumPy-Sorting means arranging elements in ascending or descending order.
1. np.sort()-Returns a sorted copy of the array.
Parameters
a → Input array
axis (optional) → Direction of sorting
kind (optional) → Sorting algorithm

2. array.sort() – Sorts the array in-place (original array is modified).

Parameters
No extra parameter required (works on array directly)

3. Sorting 2D Arrays– Sorting can be done row-wise or column-wise.

Parameters
axis = 0 → Column-wise
axis = 1 → Row-wise

4. np.argsort() – Returns indices of sorted elements.
Parameters
a → Input array

5. np.sort_complex() – Sorts complex numbers (real part first, then imaginary).
'''
import numpy as np
# 61. Sort a NumPy array in ascending order.
arr1 = np.array([5, 2, 8, 1, 3])
result = np.sort(arr1)
print("Ascending order:",result)

# 62. Sort a NumPy array in descending order.
result2 = np.sort(arr1)[::-1]
print("Descending order:",result2)

# 63. Sort a 2D NumPy array along a specific axis.
arr3 = np.array([[1,4,2,8,6,9],
                 [11,14,12,7,5,0]])
result3 = np.sort(arr3, axis=0)
print("Sorting along a specific axis:",result3)

# 64. Find the k smallest values in a NumPy array.
min_value = np.argmin(arr3)
print("smallest value:",min_value)

# 65. Find the k largest values in a NumPy array.
max_value = np.argmax(arr3)
print("largest value:",max_value)

# 66. Use argsort() to get the sorted indices of an array.
# Returns the indices that would sort an array (in ascending order).
result5 = np.argsort(arr3)
print("Sorted indices:",result5)

# 67. Search for a specific value in an array and return its index.
result6 = np.where(arr3 == 14)
print("Index:",result6)

# 68. Find the first occurrence of an element greater than a given value.
index = np.where(arr1 == 8)[0][0]
print("First occurance:",index)

# 69. Use where() to replace values based on a condition.
replace = np.where(arr1 == 2,0,arr1)
print(replace)
# 70. Count the occurrences of a specific value in an array.
a = np.array([1, 2, 2, 3, 2, 4])

count = np.count_nonzero(a == 2)
print(count)