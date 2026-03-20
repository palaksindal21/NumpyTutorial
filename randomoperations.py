'''
Random Number Generation
Random number generation in NumPy means creating numbers (or arrays of numbers) that follow specific probability distributions. It is widely used in simulations, machine learning, games, and testing.
NumPy provides a module: numpy.random
1. Basic Random Functions--
a.rand()- Generates random numbers uniformly between 0 and 1
Parameters:d0, d1, ..., dn → shape of array

b.randn()-Generates numbers from standard normal distribution (mean=0, std=1)
Parameters:Shape of array

c.randint()-Generates random integers
Parameters:
low → starting value (inclusive)
high → ending value (exclusive)
size → shape of output

random()-Same as rand() but takes shape as tuple

2. Advanced Random Functions--
choice()-Selects random elements from a list
Parameters:
a → input array
size → number of elements
replace → True/False (with or without repetition)
p → probability distribution

uniform()-Generates numbers in a given range
Parameters:
low, high
size

shuffle()-Shuffles array in-place

permutation()- Returns shuffled array (without modifying original)

3. Seeding --
seed()-Used to generate same random numbers every time (for reproducibility)


'''
import random
import numpy as np

a = np.random.rand(3,2)
print("3X2 matrix:",a)

b = np.random.randn(2,3)
print("randn():",b)

c = np.random.randint(1,10, size=(3,3))
print("ranint():",c)

d = np.random.random((2,2))
print("random():",d)

lst = [10,20,30,40,50,60]
e = np.random.choice(lst, size=2)
print("choice():",e)

f = np.random.uniform(5,20, size=3)
print("uniform():",f)

g = np.array([1,2,3,4,5,6])
np.random.shuffle(g)
print("shuffle():",g)

h = np.random.permutation([1,3,5,7])
print("permutation():",h)

np.random.seed(5)
print("seed():",np.random.rand(4))

# 81. Generate a random integer between 10 and 50
arr1 = np.random.randint(10,50,size=(3,3))
print("Array of numbers between 10 to 50",arr1)

# 82. Generate an array of 5 random integers between 1 and 100.
arr2 = np.random.randint(1,100,size=5)
print(arr2)

# 83. Generate an array of random numbers following a normal distribution.
arr3 = np.random.randn(3,3)
print(arr3)

# 84. Generate a 3x3 matrix with random values between -1 and 1.
arr4 = np.random.uniform(-1,1,size=(3,3))
print(arr4)

# 85. Shuffle the elements of a NumPy array randomly.
arr5 = np.array([10,20,30,40,50])
print(np.random.shuffle(arr5))

# 86. Set a random seed and generate the same random numbers
np.random.seed(10)
print(np.random.rand(4))

#87. Sample 5 random elements from a given array.
arr = np.array([10, 20, 30, 40, 50, 60, 70])
sample = np.random.choice(arr,size=5)
print(sample)

# 88. Generate a random permutation of numbers from 0 to 9.
arr6 = np.random.permutation([0,1,2,3,4,5,6,7,8,9])
print(arr6)

# 89. Generate a 2D array of random integers with a specific shape.
arr7 = np.random.randint(1, 50, size=(3, 4))
print(arr7)

# 90. Create a random matrix and compute its covariance.
data = np.random.rand(3, 5)
print("Random Matrix:\n", data)
cov_matrix = np.cov(data)
print("\nCovariance Matrix:\n", cov_matrix)
