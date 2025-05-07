# as the project is divided into several files, we need to import the functions from other files
# data_loader is a package where we loading dataset form a file
from data_loader import data_load as dl

# column_extractor is a package where we create columns for each variable by extracting an index element for each variable
from column_extractor import column_create

# summary is a package where we sum the values of each column
from summary import sum_items 

# convert_list_to_float is a package where we convert the string values to float values to be able to do math operation
from convert_list_to_float import converter

# importing an output package to output the results to a file
from output_summary_in_file import output_txt


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
    
    # Now we need to convert the string values to float values for the summary function
    float_sepal_length_var = converter(sepal_length_var)
    float_sepal_width_var = converter(sepal_width_var)
    float_petal_length_var = converter(petal_length_var)
    float_petal_width_var = converter(petal_width_var)    
     
    # using summary function to get the sum of each column
    sum_sepal_length_var = sum_items(float_sepal_length_var)
    sum_sepal_width_var = sum_items(float_sepal_width_var)
    sum_petal_length_var = sum_items(float_petal_length_var)
    sum_petal_width_var = sum_items(float_petal_width_var)
    
    # Output the results to the file 
    # Using round() method to round the result and write the output in 2 decimal places
    # https://www.geeksforgeeks.org/round-function-python/
    output_txt("Summary of sepal_length variable is: ", round(sum_sepal_length_var,2) )
    output_txt("Summary of sepal_width variable is: ", round(sum_sepal_width_var,2) )
    output_txt("Summary of petal_length variable is: ", round(sum_petal_length_var,2))
    output_txt("Summary of petal_width variable is: ", round(sum_petal_width_var,2))
    
   


