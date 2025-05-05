# 1. Outputs a summary of each variable to a single text file

# First we need to get an access to our dataset
# To read a file we use 'r' argument
# https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern
with open('iris/iris.data', 'r') as f:
    data = f.read()  # the output is a list of string type.
    
# https://docs.python.org/3.6/library/stdtypes.html#str.split
# each row is separated by a new line character, so we split the string into a list of strings
arr_string = data.split('\n') 


# creating an empy list where we will add frst item from each row
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# Creating a correct order of variables from the columns
sepal_length_var = []  
sepal_width_var = []
petal_length_var = []
petal_width_var = []

column_index = 0  # iterate throwugh the items in a list

    

# As we need to create for columns, its better to create a function that will do the same job for each column
def column_create(column, index):
    # looping through the whole arr_string list, extracting the first item from each row
    for each_row in arr_string:
        # in dataset file last two rows are empty, so we need to skip them and add only items with numbers
        if each_row == '':
            continue
        # we split each row by comma and add the first item to the column_1 list
        column.append(each_row.split(',')[index])  

column_create(sepal_length_var, 0)  # first column
column_create(sepal_width_var, 1)  # second column
column_create(petal_length_var, 2)  # third column
column_create(petal_width_var, 3)  # fourth column

print(sepal_length_var)  # print the first column

# Now we need to get an access to the first variable. 
