# Iris Dataset Analysis

This project analyzes the famous [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) by extracting columns, converting data types, and calculating summary statistics such as the sum of each column.

---

## Project Overview

The project is divided into multiple modules for better organization:

1. **`data_loader`**: Loads the dataset from a file.
2. **`column_extractor`**: Extracts specific columns from the dataset based on an index.
3. **`convert_list_to_float`**: Converts string values in a list to float values for mathematical operations.
4. **`summary`**: Provides functions to calculate summary statistics, such as the sum of column values.
5. **`analysis.py`**: The main script that ties everything together and performs the analysis.
6. **`hist_variables`**: Generates histograms and scatter plots for visualizing two variables.

---

## Features

- **Load Dataset**: Reads the Iris dataset from a file.
- **Column Extraction**: Extracts specific columns (e.g., sepal length, sepal width, petal length, petal width).
- **Data Conversion**: Converts string values to floats for numerical operations.
- **Summary Statistics**: Calculates the sum of each column.
- **Histogram Generation**: Creates histograms for each variable and saves them as PNG files.
- **Scatter Plot Generation**: Creates scatter plots for pairs of variables and saves them as PNG files.


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