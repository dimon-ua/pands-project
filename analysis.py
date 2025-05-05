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
column_1 = []  


# looping through the whole arr_string list, extracting the first item from each row
for each_row in arr_string:
    # in dataset file last two rows are empty, so we need to skip them and add only items with numbers
    if each_row == '':
        continue
    # we split each row by comma and add the first item to the column_1 list
    column_1.append(each_row.split(',')[0])      

    
print(column_1[-1])
# print(column_1)  # we print the first column






# Now we need to get an access to the first variable. 
