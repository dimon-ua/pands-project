# Iris Dataset Analysis

This project analyzes the famous [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) by extracting columns, converting data types, and calculating summary statistics such as the sum of each column.  It contains 150 samples of iris flowers, with measurements for four features:

- Sepal Length (in cm): The length of the sepal, which is the outer part of the flower.
- Sepal Width (in cm): The width of the sepal.
- Petal Length (in cm): The length of the petal, which is the inner part of the flower.
- Petal Width (in cm): The width of the petal.
- 
Each sample is labeled with one of three species of iris flowers:  

- Iris-setosa
- Iris-versicolor
- Iris-virginica

---
## References

1. **Iris Dataset**:
   - Wikipedia: [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
   - UCI Machine Learning Repository: [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris)

2. **Python Libraries**:
   - Matplotlib: [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
   - NumPy: [NumPy Documentation](https://numpy.org/doc/stable/)
   - Python Statistics Module: [Python Statistics Documentation](https://docs.python.org/3/library/statistics.html)

3. **Data Analysis Techniques**:
   - Scatter Plots: [Matplotlib Scatter Plot Tutorial](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter.html)
   - Histograms: [Matplotlib Histogram Tutorial](https://matplotlib.org/stable/gallery/statistics/hist.html)
   - Correlation Coefficient: [NumPy Correlation Coefficient](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)

4. **Markdown Formatting**:
   - Markdown Guide: [Basic Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
  

## Project Overview

The project is divided into multiple modules for better organization:

1. **`data_loader`**: Loads the dataset from a file.
2. **`column_extractor`**: Extracts specific columns from the dataset based on an index.
3. **`convert_list_to_float`**: Converts string values in a list to float values for mathematical operations.
4. **`summary`**: Provides functions to calculate summary statistics, such as the sum of column values.
5. **`analysis.py`**: The main script that ties everything together and performs the analysis.
6. **`hist_variables`**: Generates histograms and scatter plots for visualizing two variables.
7. **`mean_median_std_statistics`**: Calculates advanced statistical metrics (mean, median, and standard deviation) for each variable.
8. **`analysis.py`**: The main script that ties everything together and performs the analysis.

---

## Features

- **Load Dataset**: Reads the Iris dataset from a file.
- **Column Extraction**: Extracts specific columns (e.g., sepal length, sepal width, petal length, petal width).
- **Data Conversion**: Converts string values to floats for numerical operations.
- **Summary Statistics**: Calculates the sum of each column.
- **Histogram Generation**: Creates histograms for each variable and saves them as PNG files.
- **Scatter Plot Generation**: Creates scatter plots for pairs of variables and saves them as PNG files.
- **Advanced Statistics**: Calculates mean, median, and standard deviation for each variable.


---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Ensure the Iris dataset file (iris.data) is in the correct location.
3. Run the main script:
4. ```bash
   python analysis.py

## Example Output
The script calculates the sum of each column in the Iris dataset and writes the results to output.txt. Example:

- Summary of sepal_length variable is: 876.5
- Summary of sepal_width variable is: 458.6
- Summary of petal_length variable is: 563.7
- Summary of petal_width variable is: 179.9

## Advanced Statistics
The script calculates the mean, median, and standard deviation for each variable. Example:

- Sepal Length - Mean: 5.84, Median: 5.80, Std Dev: 0.83
- Sepal Width - Mean: 3.05, Median: 3.00, Std Dev: 0.43
- Petal Length - Mean: 3.76, Median: 4.35, Std Dev: 1.76
- Petal Width - Mean: 1.20, Median: 1.30, Std Dev: 0.76

### Histograms
Histograms are generated for each variable to visualize the distribution of values. Example:

- **histograms/Sepal Length.png**
- **histograms/Sepal Width.png**
- **histograms/Petal Length.png**
- **histograms/Petal Width.png**

### Scatter Plots
Scatter plots are generated to visualize relationships between pairs of variables. Example:
- **scatter_plots/Sepal Length_vs_Sepal Width.png**
- **scatter_plots/Petal Length_vs_Petal Width.png**

## Dependencies

- Python 3.x
- `matplotlib` (for plotting histograms and scatter plots)
- 
Install dependencies using:
```bash
   pip install matplotlib
   ```

## Dataset
The Iris dataset contains 150 rows and 5 columns:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Class (e.g., Iris-setosa, Iris-versicolor, Iris-virginica)