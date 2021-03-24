import numpy as np
import sys

"""
Why Numpy array is better than python lists?

numpy uses less space in memory, making it more fast to read than lists.
"""

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(c[1, 1, 1])