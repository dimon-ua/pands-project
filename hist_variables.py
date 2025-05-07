# Importing matplotlib for histograms, to plot the data
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

# Importing os to be able to store pics in a folder
# https://docs.python.org/3/library/os.html#module-os
import os

def hist_plot(column, name_variable):
            # Plotting the data, histograms on each variables
            # https://matplotlib.org/stable/gallery/statistics/hist.html
        plt.plot(column, 'r', label=name_variable)
        # Adding legend to the plot, the bane_variable is the name of the variable which will be shown in the legend
        plt.legend()
        
        # Adding title to the plot
        plt.title(name_variable + ' Histogram')
        
        # Show the plot
        # plt.show()
        
        if not os.path.exists('histograms'):
            os.makedirs('histograms')  # Create the folder if it doesn't exist
        
        # Saving the plot to a folder
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib-figure-figure-savefig
        # Using os.path.join to create the path to the folder and save the png files
        # https://docs.python.org/3/library/os.path.html
        plt.savefig(os.path.join('histograms', f'{name_variable}.png'), format='png')
        
        # Clear the plot to avoid overlapping plots in subsequent calls
        plt.clf()
        