def output_txt(name_column, variable):
    with open ('output.txt', 'a') as file:
            file.write(f'{name_column}: ' + str(variable) + '\n')
        
       
    

