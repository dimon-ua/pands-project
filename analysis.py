# 1. Outputs a summary of each variable to a single text file

# First we need to get an access to our dataset
# To read a file we use 'r' argument
# https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern
with open('iris/iris.data', 'r') as f:
    data = f.read()  # the output is a string type.
    

# Finding how many variables does this dataset has.



# Now we need to get an access to the first variable. 
