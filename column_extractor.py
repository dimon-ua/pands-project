# As we need to create four columns, its better to create a function that will do the same job for each column
def column_create(rows, index):  
    column = []
    for each_row in rows:
        
        # in dataset file last two rows are empty, so we need to skip them and add only items with numbers
        if each_row == '':
            continue
        
        # we split each row by comma and add the index item to the column list
        column.append(each_row.split(',')[index])    
    return column
     
     
    
    
