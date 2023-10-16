import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv

### Treat data from CSV file
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

def TPS_Centres(x_values):
    TPS_centres = []

    # In the mean time, just use the x values as the centres
    TPS_centres = x_values

    return TPS_centres

### Thin Plate Spline (TPS) 
def TPS_matrix_A(degree, b, TPS_Centres, x_values):
    A = np.empty((len(x_values), len(TPS_Centres)))
    a = degree
    b = b
    for i in range(len(x_values)):
        for j in range(len(TPS_Centres)):
            if TPS_Centres[j] == x_values[i]:
                A[i, j] = 0
            else:
                r = np.sqrt(np.power((TPS_Centres[j] - x_values[i]), 2))
                A[i, j] = b * np.power(r, 2*a) * np.log(b * r)
    return A