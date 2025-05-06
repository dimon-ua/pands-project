# as the project is divided into several files, we need to import the functions from other files
from data_loader import data_load as dl
from column_extractor import column_create
from summary import sum_items 


# this means that this file will be run as a script, not inported
if __name__ == "__main__":
    column = dl()  # load the dataset from the file
    # print(column)  # print the whole dataset

    # https://en.wikipedia.org/wiki/Iris_flower_data_set
    # Creating a correct order of variables from the columns 
    # [sepal_length_var, 
    # sepal_width_var, 
    # petal_length_var, 
    # petal_width_var]
    
    
    # extracting from column_create func a correct column
    sepal_length_var = column_create(column, 0)  # first column with 1st element
    sepal_width_var = column_create(column, 1)  # second column with 2nd element
    petal_length_var = column_create(column, 2)  # third column with 3rd element
    petal_width_var = column_create(column, 3)  # fourth column with 4th element
     
    print(sum_items(sepal_length_var))  # print the sum of the first column


