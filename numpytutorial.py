# Basic numpy operations
import numpy as np
# create numpy 1D array from list [1,2,3,4,5]
a = [1,2,3,4,5]

print(np.array(a))  

# Create a NumPy array of shape (3, 3) filled with zeros.
arr = np.zeros((3,3),dtype=int)
print(arr)

# Create a NumPy array of shape (2, 4) filled with ones.
arr2 = np.ones((2,4))
print(arr2)

# Generate an array of numbers from 10 to 50 with a step of 5.
arr3 = np.arange(10,50,5)
print(arr3)

#Create an array of 10 evenly spaced values between 0 and 1.
arr4 = np.linspace(0,1,10)
print(arr4)

# . Generate a 5x5 identity matrix
arr5 = np.eye(5,5)
print(arr5)

# Create an array of shape (3,3) with random values between 0 and 1.
arr6 = np.random.rand(3,3)
print(arr6)

# Convert a Python list [10, 20, 30] into a NumPy array and print its type

lst = [10,20,30]
b = np.array(lst)
print(b)
print(type(b))

# 9. Create an array of 10 random integers between 1 and 100.
arr7 = np.random.randint(1,100,10)
print(arr7)

# Generate a 4x4 array with random floating-point numbers
arr8 = np.random.rand(4,4)
print(arr8)