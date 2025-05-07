# Importing matplotlib for histograms, to plot the data
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

def hist_plot(column, name_variable):
            # Plotting the data, histograms on each variables
            # https://matplotlib.org/stable/gallery/statistics/hist.html
        plt.plot(column, 'r', label=name_variable)
        # Adding legend to the plot, the bane_variable is the name of the variable which will be shown in the legend
        plt.legend()
        
        # Adding title to the plot
        plt.title(name_variable + ' Histogram')
        
        # Show the plot
        plt.show()