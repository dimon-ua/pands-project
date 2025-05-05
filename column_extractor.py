# As we need to create for columns, its better to create a function that will do the same job for each column
def column_create(item, index):
    # looping through the whole arr_string list, extracting the first item from each row
    for each_row in item:
        # in dataset file last two rows are empty, so we need to skip them and add only items with numbers
        if each_row == '':
            continue
        # we split each row by comma and add the first item to the column_1 list
        item.append(each_row.split(',')[index])       
    
    
