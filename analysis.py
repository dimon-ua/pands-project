# 1. Outputs a summary of each variable to a single text file

# First we need to get an access to our dataset
# To read a file we use 'r' argument
# https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern
with open('iris/iris.data', 'r') as f:
    data = f.read()  # the output is a string type.
    

arr_string = data.split()  # we split the string into a list of strings

# we create an empty list for the first column
column_1 = []  

# it will iteration in next step
index = 0


# looping through the whole arr_string list, extracting the first item from each row
for each_item in arr_string:
    for each_item_index_0 in arr_string[index]:
        column_1.append(each_item_index_0)
        index += 1
        
        
print(column_1)  # we print the first column






# Now we need to get an access to the first variable. 
