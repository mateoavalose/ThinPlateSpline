import numpy as np
import pandas as pd

import csv

# Function to convert CSV file to separate arrays
def csv_to_arrays(csv_file, has_header=True):
    x_values = []
    fx_values = []
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            if has_header:
                next(csv_reader)  # Skip the header row
            for row in csv_reader:
                if len(row) >= 2:
                    x, fx = float(row[0]), float(row[1])
                    x_values.append(x)
                    fx_values.append(fx)
                else:
                    print("Skipping a row with insufficient data:", row)
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return x_values, fx_values

# Function to calculate the inverse of the A matrix and calculate the weight matrix
def invA_weight(A, fx_values):
    A_inv = np.linalg.inv(A)
    w = np.matmul(A_inv, fx_values)
    return w