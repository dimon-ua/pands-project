def data_load():
    """
    Loads the dataset from the given file path and splits it into rows.
    """
    # First we need to get an access to our dataset
    # To read a file we use 'r' argument
    # https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern
    with open('iris/iris.data', 'r') as f:
        data = f.read()  # the output is a list of string type.
        
    # https://docs.python.org/3.6/library/stdtypes.html#str.split
    # each row is separated by a new line character, so we split the string into a list of strings
    arr_string = data.split('\n') 
    return arr_string
  
