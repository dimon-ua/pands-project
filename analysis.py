from data_loader import data_load
from column_extractor import column_create



if __name__ == "__main__":
    
    # creating an empy list where we will add frst item from each row
    # https://en.wikipedia.org/wiki/Iris_flower_data_set
    # Creating a correct order of variables from the columns
    sepal_length_var = []  
    sepal_width_var = []
    petal_length_var = []
    petal_width_var = []
    
    # using the function to create each column
    column_create(sepal_length_var, 0)  # first column with 1st element
    column_create(sepal_width_var, 1)  # second column with 2nd element
    column_create(petal_length_var, 2)  # third column with 3rd element
    column_create(petal_width_var, 3)  # fourth column with 4th element

    print(sepal_length_var)  # print the first column

# Now we need to get an access to the first variable. 
