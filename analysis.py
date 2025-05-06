# as the project is divided into several files, we need to import the functions from other files
from data_loader import data_load
from column_extractor import column_create


# this means that this file will be run as a script, not inported
if __name__ == "__main__":
    data = data_load()  # calling the function to load the data from the file
    print(data)  # print the data to check if it is loaded correctly
    # creating an empy list where we will add frst item from each row
    # https://en.wikipedia.org/wiki/Iris_flower_data_set
    # Creating a correct order of variables from the columns
    sepal_length_var = []  
    sepal_width_var = []
    petal_length_var = []
    petal_width_var = []
    
    # using the function to create each column
    sepal_length_var = column_create(data, 0)  # first column with 1st element
    column_create(sepal_width_var, 1)  # second column with 2nd element
    column_create(petal_length_var, 2)  # third column with 3rd element
    column_create(petal_width_var, 3)  # fourth column with 4th element

    # print(sepal_length_var)  # print the first column


