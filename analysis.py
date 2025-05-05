# 1. Outputs a summary of each variable to a single text file


# Importing the necessary libraries to start to work with the dataset
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
from sklearn.datasets import load_iris 

# Loading the iris dataset into the data variable
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
data = load_iris()

# Getting an access to the first column of the dataset 
# The output is an array
first_variable = data['data'][:,0]
