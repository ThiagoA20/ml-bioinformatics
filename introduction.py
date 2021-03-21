""" 
import matplotlib.pyplot as plt
from sklearn import datasets

'''
Features (also know as attributes), are what compose the dimension of an model,
they are the columns of the dataset, while the rows are the instances, all of them are
independent, it means that the value are not related between themselves. They need to
be transformed in a number with value betweeen 0 and 1, this process is called preprocessing.

On the other hand, we have the labels, wich are the last column of a dataset and a dependent
variable, it means that their value will be determined by the attributes
'''

iris = datasets.load_iris()

x = iris.data
y = iris.target

print(x.shape)
# (150, 4) --> 150 instances for 4 attributes
print(y.shape) 
# (150,) --> 150 instances for 1 attribute (this is the label)

'''
The data needs to be splited between test and train.

The test data will configure the patterns
The train data will be used to check the accuracy of the algorithm

usually the test is small than the train. In the case bellow, the test have the size of 20%.
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
"""