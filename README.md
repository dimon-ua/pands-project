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

---

## Features

- **Load Dataset**: Reads the Iris dataset from a file.
- **Column Extraction**: Extracts specific columns (e.g., sepal length, sepal width, petal length, petal width).
- **Data Conversion**: Converts string values to floats for numerical operations.
- **Summary Statistics**: Calculates the sum of each column.

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

