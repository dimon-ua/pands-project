# Importing numoy package to get access to mean, median, std functions access
import numpy as np

# function to calculate mean, median and std for each variable
def calc_mean_med_std(column, column_name):
    """
    Calculate the mean, median, and standard deviation of a list of a column.
    """
    with open('statistics.txt', 'a') as file:
        # Creating vars with calculations
        column_mean = np.mean(column)
        column_median = np.median(column)
        column_std = np.std(column)
        # new txt file with statistics
        file.write(f'{column_name}, mean: {column_mean}, median: {column_median}, std: {column_std}\n')