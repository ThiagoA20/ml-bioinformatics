from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()

x = boston.data
y = boston.target

l_reg = linear_model.LinearRegression()

plt.scatter(x, y)
