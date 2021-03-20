import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""" Features (also know as attributes), are what compose the dimension of an model,
they are the columns of the dataset, while the rows are the instances, all of them are
independent, it means that the value are not related with themselves. On the other hand,
we have the labels, wich are the last column of a dataset and a dependent variable, it
means that they are the output"""

y = [i*2 for i in range(10)]
x = [i*4 for i in range(10)]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, y)
plt.show()
